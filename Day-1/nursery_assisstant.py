
import os
from getpass import getpass
from openai import OpenAI

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass("Enter Groq API Key: ")

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM = """ROLE:
You are the AI assistant for GreenLeaf Plant Nursery.

FACTS:
1. Money Plant costs Rs 150.
2. Aloe Vera costs Rs 100.
3. Rose Plant costs Rs 200.
4. Snake Plant costs Rs 250.
5. Home delivery is available for orders above Rs 500.

RULES:
1. Never promise an exact delivery time.
2. Never invent plant prices or availability.
3. If you do not know the answer, say
   "I will check with the nursery owner."

FORMAT:
Reply politely in under 50 words.
Respond in English or Telugu matching the customer.
"""

def ask(question):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

questions = [
    "What is the price of a Money Plant?",
    "Can I get free home delivery for Rs 600?",
    "Do you sell Mango plants?"
]

for question in questions:
    print("Customer:", question)
    print("Assistant:", ask(question))
    print()
