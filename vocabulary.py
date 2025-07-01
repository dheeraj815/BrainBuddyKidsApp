import streamlit as st
import random
import rewards
from datetime import datetime


def clear_vocabulary_session():
    keys = [k for k in st.session_state.keys() if k.startswith('vocab_')]
    for k in keys:
        del st.session_state[k]
    st.query_params.clear()


def run_vocabulary_quiz():
    st.header("📚 Vocabulary Quiz")

    vocab_questions = [
        {"word": "Enormous", "meaning": "Very big"},
        {"word": "Tiny", "meaning": "Very small"},
        {"word": "Brave", "meaning": "Showing courage"},
        {"word": "Beautiful", "meaning": "Very pretty"},
        {"word": "Fast", "meaning": "Moving quickly"},
        {"word": "Happy", "meaning": "Feeling joy"},
        {"word": "Cold", "meaning": "Low temperature"},
        {"word": "Kind", "meaning": "Nice to others"},
        {"word": "Jump", "meaning": "To leap up"},
        {"word": "Smart", "meaning": "Very intelligent"},
    ]

    random.shuffle(vocab_questions)
    total_questions = len(vocab_questions)

    if 'vocab_answers' not in st.session_state:
        st.session_state.vocab_answers = [""] * total_questions
        st.session_state.vocab_submitted = False

    for idx, q in enumerate(vocab_questions):
        st.write(f"**Q{idx+1}: What is the meaning of '{q['word']}'?**")
        st.session_state.vocab_answers[idx] = st.text_input(
            f"Your Answer for Q{idx+1}:", key=f"vocab_answer_{idx}")

    if not st.session_state.vocab_submitted:
        if st.button("Submit Vocabulary Quiz"):
            st.session_state.vocab_submitted = True

    if st.session_state.vocab_submitted:
        score = 0
        for idx, q in enumerate(vocab_questions):
            st.write(f"Q{idx+1}: Meaning of **{q['word']}**")
            st.write(f"👉 Your Answer: {st.session_state.vocab_answers[idx]}")
            st.write(f"✅ Correct Answer: {q['meaning']}")
            if st.session_state.vocab_answers[idx].strip().lower() == q['meaning'].lower():
                score += 1
        st.info(f"🏆 Your Vocabulary Score: {score}/{total_questions}")
        rewards.show_reward(score, total_questions)

        if 'quiz_history' not in st.session_state:
            st.session_state.quiz_history = []
        st.session_state.quiz_history.append({
            "quiz": "Vocabulary Quiz",
            "score": score,
            "total": total_questions,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if st.button("Restart Vocabulary Quiz"):
            clear_vocabulary_session()
