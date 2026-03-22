import streamlit as st
from extractor import extract_information

st.set_page_config(page_title="AI Knowledge Extraction", layout="centered")

st.title("AI Knowledge Extraction Pipeline")

st.write("Convert unstructured text into structured insights.")

text = st.text_area("Enter text (email, complaint, report, etc.)", height=200)

if st.button("Extract Insights"):

    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing..."):
            data = extract_information(text)

        if "error" in data:
            st.error("Extraction failed")
            st.write(data["raw_output"])
        else:
            st.subheader("Extracted Insights")

            st.write(f"**Category:** {data['category']}")
            st.write(f"**Sentiment:** {data['sentiment']}")
            st.write(f"**Urgency:** {data['urgency']}")
            st.write(f"**Key Issue:** {data['key_issue']}")
            st.write(f"**Suggested Action:** {data['suggested_action']}")