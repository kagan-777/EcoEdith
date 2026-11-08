import re
import streamlit as st
from streamlit_mic_recorder import mic_recorder

from backend.voice_assignment import speech_to_text
from backend.evaluate_assignment import evaluate_assignment
from backend.stats import add_voice_assignment

st.set_page_config(
    page_title="Voice Assignment",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Voice Assignment")

st.write("Record your answer and let EcoEdith evaluate it.")

# Assignment Question
question = st.text_input(
    "Assignment Question",
    placeholder="Example: Explain Inheritance in Java."
)

st.divider()

st.subheader("🎙️ Record Your Answer")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹️ Stop Recording",
    just_once=True,
    use_container_width=True
)

if audio:

    st.success("✅ Recording Completed!")

    st.audio(audio["bytes"], format="audio/wav")

    # -------------------------
    # Speech to Text
    # -------------------------
    with st.spinner("🎧 Converting Speech to Text..."):

        text = speech_to_text(audio["bytes"])

    st.success("✅ Speech Converted Successfully!")

    st.subheader("📝 Your Answer")
    st.write(text)

    st.divider()

    # -------------------------
    # Validate Question
    # -------------------------
    if question.strip() == "":

        st.warning("⚠ Please enter the assignment question.")

    else:

        # -------------------------
        # AI Evaluation
        # -------------------------
        with st.spinner("🤖 Evaluating Your Answer..."):

            evaluation = evaluate_assignment(
                question,
                text
            )

        # -------------------------
        # Extract Score
        # -------------------------
        score = 0

        match = re.search(
            r"Score\s*:\s*(\d+)",
            evaluation,
            re.IGNORECASE
        )

        if match:
            score = int(match.group(1))

        # -------------------------
        # Update Dashboard Statistics
        # -------------------------
        add_voice_assignment(score)

        # -------------------------
        # Show Evaluation
        # -------------------------
        st.subheader("📊 AI Evaluation")

        st.markdown(evaluation)