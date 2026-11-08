import streamlit as st
from backend.teaching import teach_topic
from backend.stats import add_question

st.set_page_config(
    page_title="AI Teaching Modes",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Teaching Modes")

st.write("Learn the same topic in different teaching styles.")

# User Question
question = st.text_input(
    "Enter your question",
    placeholder="Example: Explain Inheritance"
)

# Teaching Mode
mode = st.selectbox(
    "Choose Teaching Mode",
    [
        "Beginner",
        "Student",
        "Exam Revision",
        "Interview Preparation",
        "ELI5"
    ]
)

# Generate Button
if st.button("🚀 Teach Me"):

    if question.strip() == "":

        st.warning("⚠️ Please enter a question.")

    else:

        with st.spinner("🧠 Teaching..."):

            answer = teach_topic(question, mode)

            # Update Dashboard Statistics
            add_question()

        st.success("✅ Explanation Generated!")

        st.markdown(answer)