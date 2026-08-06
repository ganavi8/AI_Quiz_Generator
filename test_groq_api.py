from groq import Groq
from config import GROQ_API_KEY

print("Key Loaded:", GROQ_API_KEY[:10] + "...")

client = Groq(api_key=GROQ_API_KEY)

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Say Hello"
            }
        ]
    )

    print("Success ✅")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error ❌")
    print(e)