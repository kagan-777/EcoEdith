from backend.retriever import get_retriever
from backend.gemini import ask_gemini


def generate_flashcards():

    retriever = get_retriever()

    documents = retriever.invoke("important concepts")

    context = ""

    for doc in documents:

        page = doc.metadata.get("page", "Unknown")

        context += f"""
Page: {page}

{doc.page_content}

-------------------------
"""

    prompt = f"""
You are EcoEdith AI Tutor.

Using ONLY the uploaded study material, create exactly 10 flashcards.

Return ONLY valid JSON.

Format:

[
    {{
        "front":"Question",
        "back":"Answer",
        "page":12
    }}
]

Rules:
- Return ONLY JSON.
- No markdown.
- No explanation outside JSON.
- Keep answers short.
- Use only the uploaded study material.

Study Material:

{context}
"""

    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    return response