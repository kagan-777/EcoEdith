from backend.retriever import get_retriever
from backend.gemini import ask_gemini


def generate_study_plan(days):

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

Using ONLY the uploaded study material, create a {days}-day study plan.

Rules:
- Divide the topics equally.
- Mention what to study each day.
- Mention revision on the last day if possible.
- Use bullet points.
- Mention page numbers whenever possible.
- Return only plain text.

Study Material:

{context}
"""

    plan = ask_gemini(prompt)

    if plan is None:
        return ""

    return str(plan)