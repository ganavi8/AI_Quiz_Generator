import json
from groq import Groq
from config import GROQ_API_KEY
from config import GROQ_API_KEY

if GROQ_API_KEY:
    print("Groq Key Loaded Successfully")
else:
    print("Groq API Key Not Found")

client = Groq(api_key=GROQ_API_KEY)

# Check API Key
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please check your .env file."
    )

# Create Groq Client
client = Groq(api_key=GROQ_API_KEY)


def generate_quiz(topic, difficulty, num_questions, quiz_type):
    """
    Generate AI quiz using Groq.
    """

    prompt = f"""
Generate a {quiz_type} quiz.

Topic:
{topic}

Difficulty:
{difficulty}

Number of Questions:
{num_questions}

Return ONLY valid JSON.

JSON format:

{{
  "questions": [
    {{
      "question": "Question text",
      "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      "answer": "Correct option exactly",
      "explanation": "Short explanation"
    }}
  ]
}}

Rules:
- Create exactly {num_questions} questions.
- Each question must have exactly 4 options.
- Only one correct answer.
- Return ONLY JSON.
- Do NOT use markdown.
- Do NOT use ```json.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            response_format={"type": "json_object"}
        )

        result = response.choices[0].message.content

        data = json.loads(result)

        if "questions" not in data:
            raise Exception("Invalid response from AI.")

        return data["questions"]

    except json.JSONDecodeError:
        raise Exception("Failed to parse AI response.")

    except Exception as e:
        raise Exception(f"Quiz Generation Failed: {e}")