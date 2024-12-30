#primary, in terminal: pip install openai
#terminal : setx OPENAI_API_KEY "your_api_key_here"

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        
        {
            "role": "user",
            "content": "Você é um experiente programador !",
        }
    ],
    model="gpt-4o", # ou gpt-03.5-turbo
    max_tokens= 200,
    temperature= 0.1 #criatividade
)
print(chat_completion.choices[0].message)

