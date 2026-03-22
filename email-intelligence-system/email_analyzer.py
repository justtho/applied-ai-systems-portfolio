from openai import OpenAI

client = OpenAI()

def analyze_email(email_text):

    prompt = f"""
    Analyze the following customer email.

    Provide:
    1. Short summary
    2. Category (Complaint, Fraud Alert, Inquiry, Account Issue)
    3. Sentiment (Positive, Neutral, Negative)
    4. Suggested response

    Email:
    {email_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content