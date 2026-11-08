from backend.retriever import get_retriever
from backend.gemini import ask_gemini


def generate_notes():

    retriever = get_retriever()

    documents = retriever.invoke("important concepts")

    context = ""

    for doc in documents:

        page = doc.metadata.get("page", "Unknown")

        context += f"""
Page: {page}

{doc.page_content}

----------------------------------
"""

    prompt = f"""
You are EcoEdith AI Tutor.

Using ONLY the uploaded study material, generate concise study notes.

Rules:
- Use headings.
- Use bullet points.
- Mention important concepts.
- Mention definitions.
- Mention formulas if available.
- Mention page numbers where relevant.
- Return only plain text.

Study Material:

{context}
"""

    notes = ask_gemini(prompt)

    if notes is None:
        return ""

    return str(notes)