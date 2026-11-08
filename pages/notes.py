import streamlit as st
from backend.notes import generate_notes
from backend.stats import add_notes

st.set_page_config(
    page_title="AI Notes",
    page_icon="📒",
    layout="wide"
)

st.title("📒 AI Study Notes")

st.write("Generate concise study notes from your uploaded learning material.")

if st.button("📝 Generate Notes"):

    with st.spinner("Generating Notes..."):

        notes = generate_notes()

    # Check whether notes were generated
    if notes is None or notes.strip() == "":

        st.error("❌ No notes were generated. Please upload a document and try again.")

    else:

        # Dashboard Statistics
        add_notes()

        st.success("✅ Notes Generated Successfully!")

        st.markdown(notes)

        st.download_button(
            label="📥 Download Notes",
            data=notes,
            file_name="EcoEdith_Study_Notes.txt",
            mime="text/plain"
        )