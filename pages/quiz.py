import streamlit as st
import json
from backend.quiz import generate_quiz
from backend.stats import add_quiz

st.set_page_config(
    page_title="Quiz Generator",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI Quiz Generator")
st.write("Generate quizzes from your uploaded study material.")

# ----------------------------
# Store Quiz
# ----------------------------
if "quiz" not in st.session_state:
    st.session_state.quiz = None

# ----------------------------
# Generate Quiz
# ----------------------------
if st.button("🎯 Generate Quiz"):

    with st.spinner("Generating Quiz..."):

        quiz_text = generate_quiz()

    try:

        st.session_state.quiz = json.loads(quiz_text)

        st.success("✅ Quiz Generated Successfully!")

    except Exception as e:

        st.error("Quiz JSON parsing failed.")

        st.code(quiz_text)

        st.exception(e)

# ----------------------------
# Display Quiz
# ----------------------------
if st.session_state.quiz:

    quiz = st.session_state.quiz

    with st.form("quiz_form"):

        user_answers = []

        for i, q in enumerate(quiz):

            st.subheader(f"Q{i+1}. {q['question']}")

            ans = st.radio(
                "Choose one",
                q["options"],
                key=f"quiz_{i}"
            )

            user_answers.append(ans)

        submit = st.form_submit_button("📤 Submit Quiz")

    if submit:

        score = 0

        wrong_answers = []

        st.markdown("---")
        st.header("📊 Quiz Result")

        for i, q in enumerate(quiz):

            correct = q["options"][q["answer"]]

            st.subheader(f"Q{i+1}. {q['question']}")

            st.write(f"📝 Your Answer: **{user_answers[i]}**")

            if user_answers[i] == correct:

                score += 1

                st.success("✅ Correct")

            else:

                st.error("❌ Incorrect")

                st.success(f"Correct Answer: **{correct}**")

                wrong_answers.append(
                    {
                        "question": q["question"],
                        "your_answer": user_answers[i],
                        "correct_answer": correct,
                        "explanation": q.get("explanation", ""),
                        "page": q.get("page", "")
                    }
                )

            if q.get("explanation"):
                st.info(q["explanation"])

            if "page" in q:
                st.caption(f"📄 Source Page: {q['page']}")

            st.divider()

        percentage = round((score / len(quiz)) * 100)

        # Dashboard Update
        add_quiz(percentage)

        st.success(f"🎉 Final Score : {score}/{len(quiz)}")
        st.write(f"### Percentage : {percentage}%")

        st.progress(percentage / 100)

        if percentage >= 50:
            st.success("🎓 PASS")
        else:
            st.error("❌ FAIL")

        if wrong_answers:

            st.markdown("---")
            st.header("📚 Review Wrong Answers")

            for item in wrong_answers:

                st.subheader(item["question"])

                st.write(f"❌ Your Answer : {item['your_answer']}")

                st.write(f"✅ Correct Answer : {item['correct_answer']}")

                if item["explanation"]:
                    st.info(item["explanation"])

                st.caption(f"📄 Page : {item['page']}")

                st.divider()

        else:

            st.balloons()

            st.success("🏆 Perfect Score!")