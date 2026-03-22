EMAIL_ANALYSIS_PROMPT = """
Analyze the following customer email and return the result in JSON format.

Fields:
summary
category (Complaint, Fraud Alert, Inquiry, Account Issue)
sentiment (Positive, Neutral, Negative)
urgency (Low, Medium, High)
suggested_response

Email:
{email_text}
"""