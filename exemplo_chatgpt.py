import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set your API Key
openai.api_key = os.getenv('OPENAI_KEY')


# Function to send a question to GPT-4
def ask_to_gpt(question: str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    # Extracting the actual content message from the response
    return response


# asking the question
question = 'Quanto vendi ontem?'
answer = ask_to_gpt(question)

# Print the response
print(f'ChatGPT response: {answer}')
