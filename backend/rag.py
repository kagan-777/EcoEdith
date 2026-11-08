from backend.retriever import get_retriever
from backend.gemini import ask_gemini
from backend.history import add_history


def ask_rag(question):

    retriever = get_retriever()

    documents = retriever.invoke(question)

    print("=" * 50)
    print("Retrieved Documents:", len(documents))

    for i, doc in enumerate(documents):

        print(f"\nChunk {i+1}")

        print(doc.page_content[:300])

    print("=" * 50)

    context = ""

    source_pages = set()

    for doc in documents:

        context += doc.page_content + "\n\n"

        page = doc.metadata.get("page")

        if page is not None:

            source_pages.add(page + 1)

    prompt = f"""
You are EcoEdith, an AI Tutor.

Answer ONLY from the uploaded study material.

If the answer is not available in the uploaded document, reply exactly:

"I couldn't find this information in your uploaded learning material."

Uploaded Study Material:

{context}

Student Question:

{question}

Give a detailed educational answer.
"""

    answer = ask_gemini(prompt)

    # Save chat history
    add_history(question, answer)

    if source_pages:

        pages = ", ".join(str(page) for page in sorted(source_pages))

        answer += f"\n\n---\n📄 **Source Pages:** {pages}"

    return answer