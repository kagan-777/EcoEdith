from backend.gemini import ask_gemini


def evaluate_assignment(question, answer):

    prompt = f"""
You are an expert university professor.

Evaluate the student's answer.

Question:
{question}

Student Answer:
{answer}

Return ONLY in the following format.

Score: X/10

Feedback:
(2-3 lines)

Correct Points:
- point 1
- point 2
- point 3

Missing Points:
- point 1
- point 2

Suggestions:
- point 1
- point 2
"""

    response = ask_gemini(prompt)

    return response