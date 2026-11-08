import streamlit as st
from streamlit_mic_recorder import mic_recorder

from backend.rag import ask_rag
from backend.voice import text_to_speech
from backend.stats import add_question

st.set_page_config(
    page_title="Voice Chat",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ AI Voice Chat")

st.write("Ask questions using your voice and listen to the AI answer.")

st.info("🎤 Click the microphone below and record your question.")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹ Stop Recording",
    just_once=True,
    key="voice_recorder"
)

# Temporary text input until Speech-to-Text is added
question = st.text_input(
    "Or type your question here",
    placeholder="Example: Explain Inheritance"
)

if st.button("🚀 Ask AI"):

    if question.strip() == "":

        st.warning("Please record or type a question.")

    else:

        with st.spinner("Thinking..."):

            answer = ask_rag(question)

            add_question()

            audio_file = text_to_speech(answer)

        st.success("✅ AI Answer")

        st.markdown(answer)

        if audio_file:

            st.audio(audio_file)

            with open(audio_file, "rb") as file:

                st.download_button(
                    "📥 Download Audio",
                    file,
                    file_name="EcoEdith_Answer.mp3",
                    mime="audio/mpeg"
                )