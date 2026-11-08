import streamlit as st
from backend.stats import get_stats

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

stats = get_stats()

st.title("📊 EcoEdith Dashboard")
st.write("Track your learning progress.")

st.divider()

# =====================================================
# First Row
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💬 Questions Asked",
        stats["questions"]
    )

with col2:
    st.metric(
        "📝 Quizzes Taken",
        stats["quizzes"]
    )

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

# =====================================================
# Second Row
# =====================================================

col5, col6, col7, col8, col9 = st.columns(5)

with col5:
    st.metric(
        "📇 Flashcards",
        stats["flashcards"]
    )

with col6:
    st.metric(
        "📒 Notes",
        stats["notes"]
    )

with col7:
    st.metric(
        "📅 Study Plans",
        stats["study_plans"]
    )

with col8:
    st.metric(
        "🎤 Voice Assignments",
        stats["voice_assignments"]
    )

with col9:
    st.metric(
        "📄 Summaries",
        stats["summaries"]
    )

st.divider()

# =====================================================
# Overall Progress
# =====================================================

total = (
    stats["questions"] +
    stats["quizzes"] +
    stats["flashcards"] +
    stats["notes"] +
    stats["study_plans"] +
    stats["voice_assignments"] +
    stats["summaries"]
)

goal = 50

progress = min(total / goal, 1.0)

st.subheader("📈 Overall Learning Progress")

st.progress(progress)

st.write(f"Completed Activities: **{total}/{goal}**")

st.divider()

# =====================================================
# Voice Statistics
# =====================================================

st.subheader("🎤 Voice Assignment Statistics")

if stats["voice_assignments"] > 0:

    average_score = (
        stats["voice_total_score"] /
        stats["voice_assignments"]
    )

    col10, col11 = st.columns(2)

    with col10:
        st.metric(
            "⭐ Average Voice Score",
            f"{average_score:.1f}/10"
        )

    with col11:
        st.metric(
            "🏅 Best Voice Score",
            f"{stats['best_voice_score']}/10"
        )

else:

    st.info("No Voice Assignments completed yet.")

st.divider()

# =====================================================
# Achievements
# =====================================================

st.subheader("🏅 Achievements")

if stats["questions"] >= 10:
    st.success("💬 Curious Learner — Asked 10+ Questions")

if stats["quizzes"] >= 5:
    st.success("📝 Quiz Master — Completed 5 Quizzes")

if stats["flashcards"] >= 5:
    st.success("📇 Flashcard Creator — Generated 5 Flashcard Sets")

if stats["notes"] >= 5:
    st.success("📒 Note Expert — Generated 5 Note Sets")

if stats["study_plans"] >= 5:
    st.success("📅 Planner Pro — Created 5 Study Plans")

if stats["voice_assignments"] >= 5:
    st.success("🎤 Voice Expert — Completed 5 Voice Assignments")

if stats["summaries"] >= 5:
    st.success("📄 Summary Expert — Generated 5 Document Summaries")

if stats["best_score"] == 5:
    st.success("🏆 Perfect Quiz Score — Scored 5/5")

if stats["best_voice_score"] == 10:
    st.success("🎙️ Perfect Voice Score — Scored 10/10")

if total == 0:
    st.info("Start using EcoEdith to unlock achievements!")

st.divider()

st.caption("EcoEdith AI Tutor • Student Dashboard")