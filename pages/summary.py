import streamlit as st

from backend.summary import generate_summary
from backend.stats import add_summary

st.set_page_config(
    page_title="AI PDF Summary",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI PDF Summary")

st.write("Generate a concise summary from your uploaded learning material.")

if st.button("📄 Generate Summary"):

    with st.spinner("Generating Summary..."):

        summary = generate_summary()

    if summary is None or summary.strip() == "":

        st.error("❌ No summary generated.")

    else:

        # Dashboard Statistics Update
        add_summary()

        st.success("✅ Summary Generated Successfully!")

        st.markdown(summary)

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="EcoEdith_Summary.txt",
            mime="text/plain"
        )