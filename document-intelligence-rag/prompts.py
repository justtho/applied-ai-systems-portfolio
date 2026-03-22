RAG_PROMPT = """
You are a helpful assistant. Use only the provided context to answer the question.
If the answer is not in the context, say you do not know.

Context:
{context}

Question:
{question}

Answer:
"""

EVALUATION_PROMPT = """
You are evaluating the quality of a RAG answer.

Return only valid JSON in this format:
{{
  "relevance_score": 0,
  "grounded_score": 0,
  "completeness_score": 0,
  "comments": ""
}}

Question:
{question}

Context:
{context}

Answer:
{answer}
"""