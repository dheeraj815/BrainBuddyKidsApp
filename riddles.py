import streamlit as st
import random
import rewards
from datetime import datetime


def clear_riddles_session():
    keys = [k for k in st.session_state.keys() if k.startswith('riddle_')]
    for k in keys:
        del st.session_state[k]
    st.query_params.clear()
    if 'riddle_answers' in st.session_state:
        del st.session_state['riddle_answers']
    if 'riddle_submitted' in st.session_state:
        del st.session_state['riddle_submitted']


def run_riddles():
    st.header("🧠 Riddles Quiz")

    riddles_questions = [
        {"question": "I’m tall when I’m young, and short when I’m old. What am I?", "answer": "A candle"},
        {"question": "What has keys but can't open doors?", "answer": "A piano"},
        {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "An echo"},
        {"question": "What can travel around the world while staying in the same spot?", "answer": "A stamp"},
        {"question": "What has hands but can’t clap?", "answer": "A clock"},
        {"question": "What comes down but never goes up?", "answer": "Rain"},
        {"question": "What has to be broken before you can use it?", "answer": "An egg"},
        {"question": "What gets wetter the more it dries?", "answer": "A towel"},
        {"question": "What has a head and a tail but no body?", "answer": "A coin"},
        {"question": "What has one eye but cannot see?", "answer": "A needle"},
        {"question": "What begins with T, ends with T, and has T in it?", "answer": "A teapot"},
        {"question": "What has cities, but no houses; forests, but no trees; and water, but no fish?", "answer": "A map"},
        {"question": "What can you catch, but not throw?", "answer": "A cold"},
        {"question": "What has many teeth, but cannot bite?", "answer": "A comb"},
        {"question": "What has a neck but no head?", "answer": "A bottle"},
        {"question": "What has an eye but can’t see?", "answer": "A needle"},
        {"question": "The more of this there is, the less you see. What is it?", "answer": "Darkness"},
        {"question": "What has to be broken before you can use it?", "answer": "An egg"},
        {"question": "What has one head, one foot, and four legs?", "answer": "A bed"},
        {"question": "What goes up but never comes down?", "answer": "Your age"},
        {"question": "What has lots of eyes, but can’t see?", "answer": "A potato"},
        {"question": "What gets bigger the more you take away?", "answer": "A hole"},
        {"question": "What has a heart that doesn’t beat?", "answer": "An artichoke"},
        {"question": "What can fill a room but takes up no space?", "answer": "Light"},
        {"question": "What has a thumb and four fingers but is not a hand?", "answer": "A glove"},
        {"question": "What runs but never walks?", "answer": "A river"},
        {"question": "What has legs but doesn’t walk?", "answer": "A table"},
        {"question": "What has a face and two hands but no arms or legs?", "answer": "A clock"},
        {"question": "What is full of holes but still holds water?", "answer": "A sponge"},
        {"question": "What kind of band never plays music?", "answer": "A rubber band"},
        {"question": "What has to be broken before you use it?", "answer": "An egg"},
        {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "The letter M"},
        {"question": "What has ears but cannot hear?", "answer": "A cornfield"},
        {"question": "What can be broken but never held?", "answer": "A promise"},
        {"question": "What goes through towns and over hills but never moves?", "answer": "A road"},
        {"question": "What has hands but can’t hold anything?", "answer": "A clock"},
        {"question": "What can travel around the world while staying in one spot?", "answer": "A stamp"},
        {"question": "What has a neck but no head?", "answer": "A bottle"},
        {"question": "What begins with an E but only has one letter?", "answer": "An envelope"},
        {"question": "What has 13 hearts but no other organs?", "answer": "A deck of cards"},
        {"question": "What has a ring but no finger?", "answer": "A telephone"},
        {"question": "What kind of tree can you carry in your hand?", "answer": "A palm"},
        {"question": "What word is spelled incorrectly in every dictionary?", "answer": "Incorrectly"},
        {"question": "What has four wheels and flies?", "answer": "A garbage truck"},
        {"question": "What can fill a room but takes up no space?", "answer": "Light"},
        {"question": "What has a bottom at the top?", "answer": "A leg"},
        {"question": "What begins with T, ends with T, and has T in it?", "answer": "A teapot"},
        {"question": "What is always in front of you but can’t be seen?", "answer": "The future"},
    ]

    random.shuffle(riddles_questions)
    total_questions = len(riddles_questions)

    if 'riddle_answers' not in st.session_state:
        st.session_state.riddle_answers = [""] * total_questions
        st.session_state.riddle_submitted = False

    for idx, q in enumerate(riddles_questions):
        st.write(f"**Q{idx + 1}: {q['question']}**")
        st.session_state.riddle_answers[idx] = st.text_input(
            f"Your Answer for Q{idx + 1}:", key=f"riddle_answer_{idx}")

    if not st.session_state.riddle_submitted:
        if st.button("Submit Riddles Quiz"):
            st.session_state.riddle_submitted = True

    if st.session_state.riddle_submitted:
        score = 0
        for idx, q in enumerate(riddles_questions):
            st.write(f"Q{idx + 1}: {q['question']}")
            st.write(f"👉 Your Answer: {st.session_state.riddle_answers[idx]}")
            st.write(f"✅ Correct Answer: {q['answer']}")
            if st.session_state.riddle_answers[idx].strip().lower() == q['answer'].lower():
                score += 1

        st.info(f"🏆 Your Riddles Score: {score}/{total_questions}")
        rewards.show_reward(score, total_questions)

        # Save to quiz history for parent dashboard
        if 'quiz_history' not in st.session_state:
            st.session_state.quiz_history = []
        st.session_state.quiz_history.append({
            "quiz": "Riddles Quiz",
            "score": score,
            "total": total_questions,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if st.button("Restart Riddles Quiz"):
            clear_riddles_session()
            st.experimental_rerun()