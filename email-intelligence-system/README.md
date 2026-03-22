# Email Intelligence System

## Overview
This project is an AI-powered email analysis system that extracts key insights from unstructured email content.

## Features
- Sentiment detection  
- Urgency classification  
- Category identification  
- Key issue extraction  
- Suggested action generation  

## How It Works
The system uses an LLM-based extraction pipeline to convert email text into structured JSON output.

Email Text → LLM → Structured Insights


## Example Use Case
- Customer support automation  
- Financial crime alerts  
- Complaint classification  

## Tech Stack
- Python  
- OpenAI API  
- Streamlit  

## Run the App
```bash
streamlit run app.py

Output Example
{
  "category": "Fraud Alert",
  "sentiment": "Negative",
  "urgency": "High",
  "key_issue": "Unauthorized transaction detected",
  "suggested_action": "Investigate account and secure access"
}