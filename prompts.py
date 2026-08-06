def generate_quiz_prompt(topic, difficulty, num_questions, quiz_type):

    return f"""
You are an expert quiz creator.

Generate exactly {num_questions} {quiz_type} questions.

Topic:
{topic}

Difficulty:
{difficulty}

Rules:

1. Return ONLY valid JSON.
2. Do NOT use markdown.
3. Do NOT write explanations outside JSON.
4. Every question must contain:
   - question
   - options (exactly 4)
   - answer
   - explanation

Format:

[
    {{
        "question":"Question",
        "options":[
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "answer":"Option A",
        "explanation":"Reason"
    }}
]
"""