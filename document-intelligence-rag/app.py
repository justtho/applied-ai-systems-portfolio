import os
import tempfile
import streamlit as st

from document_loader import load_document
from rag_pipeline import create_vector_store, ask_question
from feedback_logger import log_feedback

st.set_page_config(page_title="Document Intelligence Assistant", layout="wide")

st.title("Document Intelligence Assistant (RAG)")

uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "last_question" not in st.session_state:
    st.session_state.last_question = ""

if "last_answer" not in st.session_state:
    st.session_state.last_answer = ""

if "last_evaluation" not in st.session_state:
    st.session_state.last_evaluation = {}

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    with st.spinner("Loading and indexing document..."):
        documents = load_document(temp_path)
        st.session_state.vector_db = create_vector_store(documents)

    os.remove(temp_path)
    st.success("Document uploaded and indexed successfully.")

question = st.text_input("Ask a question about the document")

if st.button("Ask"):
    if st.session_state.vector_db is None:
        st.warning("Please upload a PDF first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            answer, evaluation, docs = ask_question(st.session_state.vector_db, question)

        st.session_state.last_question = question
        st.session_state.last_answer = answer
        st.session_state.last_evaluation = evaluation

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Evaluation")
        st.write(f"Relevance: {evaluation.get('relevance_score', 'N/A')}")
        st.write(f"Groundedness: {evaluation.get('grounded_score', 'N/A')}")
        st.write(f"Completeness: {evaluation.get('completeness_score', 'N/A')}")
        st.write(f"Comments: {evaluation.get('comments', 'N/A')}")

        st.subheader("Retrieved Context")
        for i, doc in enumerate(docs, start=1):
            with st.expander(f"Chunk {i}"):
                st.write(doc.page_content)

if st.session_state.last_answer:
    st.subheader("Feedback")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Helpful"):
            log_feedback(
                st.session_state.last_question,
                st.session_state.last_answer,
                "Positive"
            )
            st.success("Positive feedback recorded.")

    with col2:
        if st.button("👎 Not Helpful"):
            log_feedback(
                st.session_state.last_question,
                st.session_state.last_answer,
                "Negative"
            )
            st.success("Negative feedback recorded.")