import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY is not set.")
    exit()

client = OpenAI(api_key=api_key)

question = input("You: ")

try:
    response = client.responses.create(
        model="gpt-5-mini",
        input=question,
    )
    print("Response ID:", response.id)
    print("Model:", response.model)
    print("Usage:", response.usage)
    print("AI:", response.output_text)

except RateLimitError:
    print("Error: OpenAI API quota or rate limit exceeded.")

