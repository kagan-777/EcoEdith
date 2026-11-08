import streamlit as st

from backend.history import (
    get_history,
    clear_history
)

st.set_page_config(
    page_title="Chat History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Chat History")

st.write("Review all your previous AI conversations.")

st.divider()

col1, col2 = st.columns([6, 1])

with col2:

    if st.button("🗑 Clear"):

        clear_history()

        st.success("History Cleared Successfully!")

        st.rerun()

history = get_history()

if len(history) == 0:

    st.info("No chat history available.")

else:

    for chat in history:

        with st.expander(
            f"🕒 {chat['time']}",
            expanded=False
        ):

            st.markdown("### ❓ Question")

            st.write(chat["question"])

            st.markdown("### 🤖 AI Answer")

            st.write(chat["answer"])

st.divider()

st.caption("EcoEdith AI Tutor • Chat History")