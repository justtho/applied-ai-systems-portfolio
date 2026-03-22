import streamlit as st
from email_analyzer import analyze_email

st.title("AI Email Assistant")

email = st.text_area("Paste Email Here")

if st.button("Analyze"):
    result = analyze_email(email)
    st.write(result)