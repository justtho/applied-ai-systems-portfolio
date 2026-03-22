import json
from openai import OpenAI
from prompts import EVALUATION_PROMPT

client = OpenAI()

def evaluate_answer(question, context, answer):
    prompt = EVALUATION_PROMPT.format(
        question=question,
        context=context,
        answer=answer
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "relevance_score": "N/A",
            "grounded_score": "N/A",
            "completeness_score": "N/A",
            "comments": content
        }