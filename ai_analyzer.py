import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.Client(api_key=openai.api_key)

def analyze_logs(log_text: str) -> str:
    prompt = f"""
You are an expert Flutter performance and error analysis AI.
Analyze the following logs and summarize:
1. Critical errors or repeated issues.
2. Performance bottlenecks.
3. Suggested improvements.

Logs:
{log_text}

Respond in bullet points.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": "You are a helpful software engineering assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=600,
    )

    return response.choices[0].message.content.strip()
