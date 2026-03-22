from openai import OpenAI
from prompts import EXTRACTION_PROMPT
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()


def extract_information(text: str) -> dict:
    prompt = EXTRACTION_PROMPT.format(text=text)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    result = response.choices[0].message.content

    try:
        data = json.loads(result)
        return data
    except json.JSONDecodeError:
        return {
            "error": "Failed to parse response",
            "raw_output": result
        }