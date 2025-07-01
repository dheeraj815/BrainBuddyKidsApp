import streamlit as st
import random
import rewards
from datetime import datetime


def clear_fun_facts_session():
    keys = [k for k in st.session_state.keys() if k.startswith('fun_')]
    for k in keys:
        del st.session_state[k]
    st.query_params.clear()


def run_fun_facts_quiz():
    st.header("🤓 Fun Facts Quiz")

    fun_facts_questions = [
        {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is the tallest animal in the world?", "answer": "Giraffe"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "What is the fastest land animal?", "answer": "Cheetah"},
        {"question": "Which is the largest mammal?", "answer": "Blue Whale"},
        {"question": "Which bird is known for mimicking sounds?", "answer": "Parrot"},
        {"question": "Which planet has rings around it?", "answer": "Saturn"},
        {"question": "Which animal is known as the King of the Jungle?", "answer": "Lion"},
        {"question": "What is the smallest planet in our solar system?",
            "answer": "Mercury"},
        {"question": "What gas do plants absorb?", "answer": "Carbon dioxide"},
    ]

    random.shuffle(fun_facts_questions)
    total_questions = len(fun_facts_questions)

    if 'fun_facts_answers' not in st.session_state:
        st.session_state.fun_facts_answers = [""] * total_questions
        st.session_state.fun_facts_submitted = False

    for idx, q in enumerate(fun_facts_questions):
        st.write(f"**Q{idx+1}: {q['question']}**")
        st.session_state.fun_facts_answers[idx] = st.text_input(
            f"Your Answer for Q{idx+1}:", key=f"fun_answer_{idx}")

    if not st.session_state.fun_facts_submitted:
        if st.button("Submit Fun Facts Quiz"):
            st.session_state.fun_facts_submitted = True

    if st.session_state.fun_facts_submitted:
        score = 0
        for idx, q in enumerate(fun_facts_questions):
            st.write(f"Q{idx+1}: {q['question']}")
            st.write(
                f"👉 Your Answer: {st.session_state.fun_facts_answers[idx]}")
            st.write(f"✅ Correct Answer: {q['answer']}")
            if st.session_state.fun_facts_answers[idx].strip().lower() == q['answer'].lower():
                score += 1
        st.info(f"🏆 Your Fun Facts Score: {score}/{total_questions}")
        rewards.show_reward(score, total_questions)

        if 'quiz_history' not in st.session_state:
            st.session_state.quiz_history = []
        st.session_state.quiz_history.append({
            "quiz": "Fun Facts Quiz",
            "score": score,
            "total": total_questions,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if st.button("Restart Fun Facts Quiz"):
            clear_fun_facts_session()
