
import os
from getpass import getpass
from openai import OpenAI

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass("Enter Groq API Key: ")

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a funny joker"},
        {"role": "user", "content": "tell me a joke"}
    ]
)

print(response.choices[0].message.content)
