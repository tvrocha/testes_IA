import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv('GROQ_KEY')
)


def ask_to_groq(question: str):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192"
    )

    return response.choices[0].message.content


question = 'Quanto vendi ontem?'
answer = ask_to_groq(question)

print(f'Response of Groq: {answer}')
