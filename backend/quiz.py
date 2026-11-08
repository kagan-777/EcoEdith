import re

from backend.retriever import get_retriever
from backend.gemini import ask_gemini


def generate_quiz():

    retriever = get_retriever()

    documents = retriever.invoke(
        "important concepts from the uploaded study material"
    )[:3]

    context = ""

    for doc in documents:

        page = doc.metadata.get("page", "Unknown")

        context += f"""
Page Number: {page}

Content:
{doc.page_content}

----------------------------------
"""

    prompt = f"""
You are EcoEdith AI Tutor.

Using ONLY the uploaded study material below, generate EXACTLY 3 multiple-choice questions.

Return ONLY valid JSON.

Format:

[
  {{
    "question": "Question here",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": 0,
    "explanation": "Short explanation.",
    "page": 1
  }}
]

Rules:

- Generate exactly 3 questions.
- Exactly 4 options.
- "answer" must be an integer from 0 to 3.
- Use ONLY the uploaded study material.
- No markdown.
- No code block.
- No explanation outside JSON.
- Return ONLY the JSON array.

Study Material:

{context}
"""

    response = ask_gemini(prompt) or ""

    # Remove markdown
    response = response.replace("```json", "")
    response = response.replace("```", "").strip()

    # Extract JSON array only
    match = re.search(r"\[.*\]", response, re.DOTALL)

    if match:
        response = match.group(0)

    return response