import streamlit as st
from backend.gemini import ask_gemini

st.set_page_config(
    page_title="Gemini Test",
    page_icon="🤖"
)

st.title("🤖 Gemini AI Test")

question = st.text_input("Ask Anything")

if st.button("Ask Gemini"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            answer = ask_gemini(question)

        st.success("Response Generated!")

        st.write(answer)