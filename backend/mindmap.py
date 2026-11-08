import json
import re
import os

from backend.gemini import ask_gemini


def generate_mindmap():

    # Check whether full PDF text exists
    if not os.path.exists("data/full_text.txt"):

        return json.dumps(
            {
                "root": "No PDF Uploaded",
                "branches": [
                    {
                        "title": "Upload Required",
                        "items": [
                            "Please upload a PDF first."
                        ]
                    }
                ]
            }
        )

    # Read complete PDF text
    with open(
        "data/full_text.txt",
        "r",
        encoding="utf-8"
    ) as f:

        context = f.read()

    # Limit very large PDFs
    context = context[:12000]

    prompt = f"""
You are EcoEdith AI Tutor.

Read the COMPLETE study material below.

Generate a hierarchical mind map.

Return ONLY valid JSON.

Format:

{{
    "root":"Main Topic",
    "branches":[
        {{
            "title":"Branch Name",
            "items":[
                "Keyword1",
                "Keyword2",
                "Keyword3"
            ]
        }}
    ]
}}

Rules:

- Use ONLY the uploaded study material.
- Root should be the document title or subject.
- Maximum 5 branches.
- Maximum 5 keywords per branch.
- Keywords should be short (1-3 words).
- Ignore authors.
- Ignore textbooks.
- Ignore reference books.
- Ignore page numbers.
- Ignore outcomes if they are not concepts.
- Focus only on important concepts.
- No explanations.
- No markdown.
- No code block.
- Return ONLY JSON.

Study Material:

{context}
"""

    response = ask_gemini(prompt) or ""

    # Remove markdown if present
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    # Extract JSON object
    match = re.search(r"\{.*\}", response, re.DOTALL)

    if match:
        response = match.group(0)

    try:

        json.loads(response)

        return response

    except Exception as e:

        print("\n========== GEMINI RESPONSE ==========\n")
        print(response)
        print("\n=====================================\n")
        print(e)

        return json.dumps(
            {
                "root": "Mind Map Error",
                "branches": [
                    {
                        "title": "Generation Failed",
                        "items": [
                            "Please Try Again"
                        ]
                    }
                ]
            }
        )