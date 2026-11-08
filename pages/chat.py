import streamlit as st
from backend.rag import ask_rag
from backend.stats import add_question

st.set_page_config(
    page_title="EcoEdith Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 EcoEdith AI Tutor")

st.write("Ask questions from your uploaded learning material.")

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
question = st.chat_input("Ask your question...")

if question:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = ask_rag(question)

            # Dashboard Stats
            add_question()

            st.markdown(answer)

    # Save AI Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )