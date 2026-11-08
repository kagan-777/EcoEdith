from backend.retriever import get_retriever
from backend.gemini import ask_gemini


def teach_topic(question, mode):

    retriever = get_retriever()

    documents = retriever.invoke(question)[:3]

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

Answer the user's question using ONLY the uploaded study material.

Teaching Mode:
{mode}

Question:
{question}

Study Material:
{context}

Instructions:

- Use ONLY the study material.
- Do NOT use outside knowledge.
- At the end of your answer, write:
  Source Page: <page number>
- Use the page number from the retrieved study material only.
- Adapt your explanation based on the selected teaching mode.

Teaching Modes:

Beginner:
Explain in simple words.

Student:
Explain with enough detail for college students.

Exam Revision:
Give concise points useful for exams.

Interview Preparation:
Explain with interview-focused concepts and examples.

ELI5:
Explain like you're talking to a 5-year-old child.
"""

    answer = ask_gemini(prompt)or""

    # Clean markdown if present
    answer = answer.replace("```", "")
    answer = answer.replace("```text", "")
    answer = answer.strip()

    return answer