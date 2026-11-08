import streamlit as st
import json

from backend.flashcards import generate_flashcards
from backend.stats import add_flashcards

st.set_page_config(
    page_title="Flashcards",
    page_icon="📇",
    layout="wide"
)

st.title("📇 AI Flashcard Generator")

st.write("Generate AI flashcards from your uploaded study material.")

if st.button("📚 Generate Flashcards"):

    with st.spinner("Generating Flashcards..."):

        flashcards_text = generate_flashcards()

    try:

        flashcards = json.loads(flashcards_text)

        # Dashboard Statistics
        add_flashcards()

        st.success(
            f"✅ Generated {len(flashcards)} Flashcards"
        )

        for i, card in enumerate(flashcards):

            with st.expander(f"📇 Flashcard {i+1}"):

                st.subheader("❓ Question")
                st.write(card["front"])

                st.subheader("✅ Answer")
                st.write(card["back"])

                if "page" in card:

                    try:
                        st.caption(
                            f"📄 Source Page: {card['page'] + 1}"
                        )

                    except Exception:

                        st.caption(
                            f"📄 Source Page: {card['page']}"
                        )

    except Exception as e:

        st.error("Flashcard JSON parsing failed.")

        st.code(flashcards_text)

        st.exception(e)