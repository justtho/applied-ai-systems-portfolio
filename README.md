# Applied AI Systems Portfolio

- email-intelligence-system/
- document-intelligence-rag/
- knowledge-extraction-pipeline/

This repository showcases a set of applied AI systems built to explore real-world AI architectures, including LLM-based applications, Retrieval-Augmented Generation (RAG), and structured information extraction.

---

## 🚀 Overview

The goal of this portfolio is to demonstrate how modern AI systems can process unstructured data and transform it into actionable insights across enterprise workflows.

The systems are designed with a focus on:

- End-to-end AI pipelines  
- Modular architecture  
- Evaluation and monitoring  
- Real-world business use cases  

---

## 🧠 Systems Included

### 🔹 1. Email Intelligence System
An AI assistant that analyzes incoming emails and extracts key insights.

**Capabilities:**
- Sentiment detection  
- Urgency classification  
- Category identification  
- Key issue extraction  
- Suggested action generation  

---

### 🔹 2. Document Intelligence System (RAG)
A Retrieval-Augmented Generation system that allows users to query documents using natural language.

**Capabilities:**
- Document ingestion (PDF)  
- Text chunking  
- Embedding generation  
- Vector similarity search  
- Context-aware response generation  
- Evaluation and logging  
- User feedback loop  

---

### 🔹 3. AI Knowledge Extraction Pipeline
A system that converts unstructured text into structured JSON outputs using LLMs.

**Capabilities:**
- Information extraction  
- Structured data generation  
- Reusable AI pipeline  
- Integration with other AI applications  

---

## 🏗️ Architecture Overview

The systems follow a modular AI architecture:
Unstructured Data (Emails / Documents)
↓
AI Processing Layer
(LLM + Retrieval + Extraction)
↓
Structured Insights / Answers
↓
Evaluation + Logging + Feedback

---

## 🔧 Tech Stack

- Python  
- OpenAI API  
- LangChain  
- FAISS (vector store)  
- Streamlit (UI)  

---

## ☁️ Future Direction (AWS Integration)

This architecture is designed to be extended into a cloud-native deployment using AWS services:

- Amazon S3 → document storage  
- AWS Lambda → ingestion pipelines  
- Amazon Bedrock → LLM and embeddings  
- OpenSearch → vector search  
- CloudWatch → logging and monitoring  

---

## 🎯 Use Cases

These systems are particularly relevant for:

- Financial crime investigations  
- Compliance and regulatory workflows  
- Customer support automation  
- Knowledge management systems  

---

## 📌 Key Learnings

- Building end-to-end AI systems requires more than model usage  
- Evaluation and monitoring are critical for real-world deployment  
- Structured outputs enable downstream automation and analytics  

---

## ▶️ Running the Applications

Each system can be run independently:

```bash
streamlit run app.py

👤 Author

Justy Thomas