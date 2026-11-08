from backend.retriever import get_retriever
from backend.gemini import ask_gemini


def generate_summary():

    retriever = get_retriever()

    # Retrieve important chunks from the uploaded document
    documents = retriever.invoke(
        "Give the complete summary of this document."
    )

    context = ""

    for doc in documents:
        context += doc.page_content + "\n\n"

    prompt = f"""
You are EcoEdith AI.

Using ONLY the uploaded study material below,
generate a well-structured study summary.

Requirements:

- Give the title if available.
- Explain the main concepts.
- Include important definitions.
- Include key points.
- Include formulas if present.
- Include important facts.
- Keep the summary around one page.
- Use bullet points wherever possible.
- Do NOT invent information.

Study Material:

{context}
"""

    return ask_gemini(prompt)