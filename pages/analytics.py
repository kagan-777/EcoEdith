import streamlit as st
import pandas as pd
import plotly.express as px

from backend.stats import get_stats

st.set_page_config(
    page_title="Performance Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Performance Analytics")

st.write("Monitor your EcoEdith learning progress.")

stats = get_stats()

# ======================================================
# Activity Data
# ======================================================

activity = pd.DataFrame({
    "Feature": [
        "Questions",
        "Quizzes",
        "Flashcards",
        "Notes",
        "Study Plans",
        "Voice",
        "Summaries"
    ],
    "Count": [
        stats["questions"],
        stats["quizzes"],
        stats["flashcards"],
        stats["notes"],
        stats["study_plans"],
        stats["voice_assignments"],
        stats["summaries"]
    ]
})

col1, col2 = st.columns(2)

# ======================================================
# Bar Chart
# ======================================================

with col1:

    st.subheader("📊 Activity Chart")

    fig = px.bar(
        activity,
        x="Feature",
        y="Count",
        text="Count",
        title="Learning Activities"
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# Pie Chart
# ======================================================

with col2:

    st.subheader("🥧 Activity Distribution")

    pie = px.pie(
        activity,
        names="Feature",
        values="Count",
        hole=0.45
    )

    pie.update_layout(height=450)

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

# ======================================================
# Quiz & Voice Cards
# ======================================================

col3, col4, col5 = st.columns(3)

with col3:

    st.metric(
        "🏆 Best Quiz Score",
        stats["best_score"]
    )

with col4:

    st.metric(
        "🎤 Best Voice Score",
        f"{stats['best_voice_score']}/10"
    )

with col5:

    if stats["voice_assignments"] > 0:

        average = (
            stats["voice_total_score"] /
            stats["voice_assignments"]
        )

    else:

        average = 0

    st.metric(
        "⭐ Average Voice Score",
        f"{average:.1f}/10"
    )

st.divider()

# ======================================================
# Feature Usage Table
# ======================================================

st.subheader("📋 Usage Summary")

st.dataframe(
    activity,
    use_container_width=True,
    hide_index=True
)

st.caption("EcoEdith Analytics Dashboard")