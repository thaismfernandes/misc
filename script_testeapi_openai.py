import os
from openai import OpenAI

client = OpenAI(
    # INSERT OPENAI KEY BELOW OR DEFINE ENVIRONMENT VARIABLE (RECOMMENDED)
    api_key= "INSERT OPEN AI API KEY HERE",
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)


print(response.choices[0].message.content)
