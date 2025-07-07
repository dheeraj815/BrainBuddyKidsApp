import streamlit as st
import random
import rewards
from datetime import datetime


def clear_vocabulary_session():
    keys = [k for k in st.session_state.keys() if k.startswith('vocab_')]
    for k in keys:
        del st.session_state[k]
    st.query_params.clear()
    if 'vocab_answers' in st.session_state:
        del st.session_state['vocab_answers']
    if 'vocab_submitted' in st.session_state:
        del st.session_state['vocab_submitted']


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
        {"word": "Bright", "meaning": "Giving off much light"},
        {"word": "Loud", "meaning": "Making a lot of noise"},
        {"word": "Soft", "meaning": "Not hard or firm"},
        {"word": "Strong", "meaning": "Having great power"},
        {"word": "Clean", "meaning": "Free from dirt"},
        {"word": "Dark", "meaning": "Having little or no light"},
        {"word": "Cold", "meaning": "Low temperature"},
        {"word": "Quick", "meaning": "Fast"},
        {"word": "Slow", "meaning": "Not fast"},
        {"word": "Funny", "meaning": "Causing laughter"},
        {"word": "Sad", "meaning": "Feeling sorrow"},
        {"word": "Tall", "meaning": "Of great height"},
        {"word": "Short", "meaning": "Not tall"},
        {"word": "Warm", "meaning": "Moderately hot"},
        {"word": "Wet", "meaning": "Covered with water"},
        {"word": "Dry", "meaning": "Free from moisture"},
        {"word": "Young", "meaning": "Not old"},
        {"word": "Old", "meaning": "Having lived a long time"},
        {"word": "Rich", "meaning": "Having lots of money"},
        {"word": "Poor", "meaning": "Having little money"},
        {"word": "Happy", "meaning": "Feeling pleasure"},
        {"word": "Angry", "meaning": "Feeling mad"},
        {"word": "Safe", "meaning": "Free from danger"},
        {"word": "Dangerous", "meaning": "Likely to cause harm"},
        {"word": "Clean", "meaning": "Not dirty"},
        {"word": "Dirty", "meaning": "Not clean"},
        {"word": "Easy", "meaning": "Not difficult"},
        {"word": "Hard", "meaning": "Difficult"},
        {"word": "Friendly", "meaning": "Kind and pleasant"},
        {"word": "Hungry", "meaning": "Feeling the need for food"},
        {"word": "Thirsty", "meaning": "Feeling the need for drink"},
        {"word": "Beautiful", "meaning": "Very pretty"},
        {"word": "Ugly", "meaning": "Not attractive"},
        {"word": "Bright", "meaning": "Giving off much light"},
        {"word": "Dark", "meaning": "Having little light"},
        {"word": "Strong", "meaning": "Having great power"},
        {"word": "Weak", "meaning": "Not strong"},
        {"word": "Fast", "meaning": "Moving quickly"},
        {"word": "Slow", "meaning": "Not fast"},
        {"word": "Happy", "meaning": "Feeling joy"},
        {"word": "Sad", "meaning": "Feeling sorrow"},
    ]

    random.shuffle(vocab_questions)
    total_questions = len(vocab_questions)

    if 'vocab_answers' not in st.session_state:
        st.session_state.vocab_answers = [""] * total_questions
        st.session_state.vocab_submitted = False

    for idx, q in enumerate(vocab_questions):
        st.write(f"**Q{idx + 1}: What is the meaning of '{q['word']}'?**")
        st.session_state.vocab_answers[idx] = st.text_input(
            f"Your Answer for Q{idx + 1}:", key=f"vocab_answer_{idx}")

    if not st.session_state.vocab_submitted:
        if st.button("Submit Vocabulary Quiz"):
            st.session_state.vocab_submitted = True

    if st.session_state.vocab_submitted:
        score = 0
        for idx, q in enumerate(vocab_questions):
            st.write(f"Q{idx + 1}: Meaning of **{q['word']}**")
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
            st.experimental_rerun()