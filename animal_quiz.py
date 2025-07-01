import streamlit as st
import random
import rewards
from datetime import datetime


def clear_animal_quiz_session():
    keys = [k for k in st.session_state.keys() if k.startswith('animal_')]
    for k in keys:
        del st.session_state[k]
    st.query_params.clear()


def run_animal_quiz():
    st.header("🐾 Animal Quiz")

    animal_questions = [
        {"question": "Which animal is known as the King of the Jungle?", "answer": "Lion"},
        {"question": "Which animal is the largest mammal?", "answer": "Blue Whale"},
        {"question": "Which bird is known for its beautiful tail?", "answer": "Peacock"},
        {"question": "Which animal is known for building dams?", "answer": "Beaver"},
        {"question": "Which insect makes honey?", "answer": "Bee"},
        {"question": "Which animal has a long trunk?", "answer": "Elephant"},
        {"question": "Which bird cannot fly?", "answer": "Ostrich"},
        {"question": "Which animal has black and white stripes?", "answer": "Zebra"},
        {"question": "Which marine animal has eight legs?", "answer": "Octopus"},
        {"question": "Which animal is known for hopping?", "answer": "Kangaroo"},
    ]

    random.shuffle(animal_questions)
    total_questions = len(animal_questions)

    if 'animal_answers' not in st.session_state:
        st.session_state.animal_answers = [""] * total_questions
        st.session_state.animal_submitted = False

    for idx, q in enumerate(animal_questions):
        st.write(f"**Q{idx+1}: {q['question']}**")
        st.session_state.animal_answers[idx] = st.text_input(
            f"Your Answer for Q{idx+1}:", key=f"animal_answer_{idx}")

    if not st.session_state.animal_submitted:
        if st.button("Submit Animal Quiz"):
            st.session_state.animal_submitted = True

    if st.session_state.animal_submitted:
        score = 0
        for idx, q in enumerate(animal_questions):
            st.write(f"Q{idx+1}: {q['question']}")
            st.write(f"👉 Your Answer: {st.session_state.animal_answers[idx]}")
            st.write(f"✅ Correct Answer: {q['answer']}")
            if st.session_state.animal_answers[idx].strip().lower() == q['answer'].lower():
                score += 1
        st.info(f"🏆 Your Animal Quiz Score: {score}/{total_questions}")
        rewards.show_reward(score, total_questions)

        if 'quiz_history' not in st.session_state:
            st.session_state.quiz_history = []
        st.session_state.quiz_history.append({
            "quiz": "Animal Quiz",
            "score": score,
            "total": total_questions,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if st.button("Restart Animal Quiz"):
            clear_animal_quiz_session()
