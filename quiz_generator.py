import json
import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def generate_quiz(topic, difficulty, num_questions, quiz_type):

    prompt = f"""
Generate a {quiz_type} quiz.

Topic:
{topic}

Difficulty:
{difficulty}

Number of Questions:
{num_questions}

Return ONLY JSON.

JSON format:

{{
 "questions":[
   {{
    "question":"Question text",
    "options":[
       "Option A",
       "Option B",
       "Option C",
       "Option D"
    ],
    "answer":"Correct option exactly",
    "explanation":"Short explanation"
   }}
 ]
}}

Rules:
- Create exactly {num_questions} questions.
- Each question must have 4 options.
- Only one correct answer.
- No markdown.
"""

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

    return data["questions"]