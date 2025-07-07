import streamlit as st
import random
import rewards
from datetime import datetime


def clear_math_quiz_session():
    keys = [k for k in st.session_state.keys() if k.startswith('math_')]
    for k in keys:
        del st.session_state[k]
    st.query_params.clear()


def run_math_quiz():
    st.header("🧮 Math Quiz")
    total_questions = 50

    if 'math_quiz_data' not in st.session_state:
        st.session_state.math_quiz_data = []
        st.session_state.math_submitted = False
        for _ in range(total_questions):
            num1, num2 = random.randint(1, 20), random.randint(1, 20)
            st.session_state.math_quiz_data.append({
                "question": f"{num1} × {num2} = ?",
                "correct_answer": str(num1 * num2),
                "user_answer": ""
            })

    for idx, q in enumerate(st.session_state.math_quiz_data):
        st.write(f"**Q{idx+1}: {q['question']}**")
        q['user_answer'] = st.text_input(
            f"Your Answer for Q{idx+1}:", key=f"math_answer_{idx}")

    if not st.session_state.math_submitted:
        if st.button("Submit Math Quiz"):
            st.session_state.math_submitted = True

    if st.session_state.math_submitted:
        score = sum(1 for q in st.session_state.math_quiz_data if q['user_answer'].strip(
        ) == q['correct_answer'])
        for idx, q in enumerate(st.session_state.math_quiz_data):
            st.write(f"Q{idx+1}: {q['question']}")
            st.write(f"👉 Your Answer: {q['user_answer']}")
            st.write(f"✅ Correct Answer: {q['correct_answer']}")
        st.info(f"🏆 Your Math Score: {score}/{total_questions}")
        rewards.show_reward(score, total_questions)

        if 'quiz_history' not in st.session_state:
            st.session_state.quiz_history = []
        st.session_state.quiz_history.append({
            "quiz": "Math Quiz",
            "score": score,
            "total": total_questions,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if st.button("Restart Math Quiz"):
            clear_math_quiz_session()
