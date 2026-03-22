EXTRACTION_PROMPT = """
You are an AI system that extracts structured information.

Analyze the text and return ONLY valid JSON in this format:

{{
  "category": "",
  "sentiment": "",
  "urgency": "",
  "key_issue": "",
  "suggested_action": ""
}}

Rules:
- category: short label (e.g., Fraud Alert, Complaint, Inquiry)
- sentiment: Positive, Neutral, or Negative
- urgency: Low, Medium, or High
- key_issue: short summary of main issue
- suggested_action: recommended next step

Text:
{text}
"""