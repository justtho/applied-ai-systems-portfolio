from dotenv import load_dotenv
load_dotenv()
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from openai import OpenAI
from prompts import RAG_PROMPT
from evaluation import evaluate_answer

client = OpenAI()


def create_vector_store(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_documents(docs, embeddings)

    return vector_db


def ask_question(vector_db, question):
    # Step 1: Retrieve relevant docs
    retrieved_docs = vector_db.similarity_search(question, k=3)

    # Step 2: Build context
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    # Step 3: Generate answer
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    answer = response.choices[0].message.content.strip()

    # Step 4: Evaluate answer
    evaluation = evaluate_answer(question, context, answer)

    return answer, evaluation, retrieved_docs