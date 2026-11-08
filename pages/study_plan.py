import streamlit as st
from backend.study_plan import generate_study_plan
from backend.stats import add_study_plan

st.set_page_config(
    page_title="Study Planner",
    page_icon="📅",
    layout="wide"
)

st.title("📅 AI Study Planner")

st.write("Generate a personalized study plan from your uploaded learning material.")

# Select Study Duration
days = st.selectbox(
    "Select Study Duration",
    [3, 5, 7, 10, 15]
)

# Generate Button
if st.button("📅 Generate Study Plan"):

    with st.spinner("Generating Study Plan..."):

        plan = generate_study_plan(days)

    # Check if plan was generated
    if plan is None or plan.strip() == "":

        st.error("❌ No study plan generated. Please upload a document and try again.")

    else:

        # Dashboard Statistics
        add_study_plan()

        st.success("✅ Study Plan Generated Successfully!")

        st.markdown(plan)

        st.download_button(
            label="📥 Download Study Plan",
            data=plan,
            file_name=f"EcoEdith_{days}_Day_Study_Plan.txt",
            mime="text/plain"
        )