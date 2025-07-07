
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
        {"question": "Which animal is known for playing dead?", "answer": "Opossum"},
        {"question": "Which animal can rotate its head 270 degrees?", "answer": "Owl"},
        {"question": "Which animal is the tallest in the world?", "answer": "Giraffe"},
        {"question": "Which animal is known to laugh?", "answer": "Hyena"},
        {"question": "Which sea animal is dangerous and has sharp spines?", "answer": "Sea Urchin"},
        {"question": "Which animal lives in a shell and walks slowly?", "answer": "Snail"},
        {"question": "Which fish has no bones?", "answer": "Shark"},
        {"question": "Which bird mimics human speech?", "answer": "Parrot"},
        {"question": "Which insect has colorful wings?", "answer": "Butterfly"},
        {"question": "Which mammal lays eggs?", "answer": "Platypus"},
        {"question": "Which animal is famous for its quills?", "answer": "Porcupine"},
        {"question": "Which sea creature has no brain?", "answer": "Jellyfish"},
        {"question": "Which animal carries its baby in a pouch?", "answer": "Kangaroo"},
        {"question": "Which animal changes color to blend in?", "answer": "Chameleon"},
        {"question": "Which animal has the best memory?", "answer": "Elephant"},
        {"question": "Which bird is known for wisdom?", "answer": "Owl"},
        {"question": "Which insect has a hard shell and many legs?", "answer": "Beetle"},
        {"question": "Which reptile can grow back its tail?", "answer": "Lizard"},
        {"question": "Which large mammal has a horn on its nose?", "answer": "Rhinoceros"},
        {"question": "Which animal barks like a dog but is a rodent?", "answer": "Prairie Dog"},
        {"question": "Which animal produces silk?", "answer": "Silkworm"},
        {"question": "Which bird is the fastest flyer?", "answer": "Peregrine Falcon"},
        {"question": "Which mammal can fly?", "answer": "Bat"},
        {"question": "Which desert animal stores fat in its hump?", "answer": "Camel"},
        {"question": "Which animal sleeps standing up?", "answer": "Horse"},
        {"question": "Which animal lives both in water and on land?", "answer": "Frog"},
        {"question": "Which bird lays the largest egg?", "answer": "Ostrich"},
        {"question": "Which animal is known for spinning webs?", "answer": "Spider"},
        {"question": "Which sea creature has arms called tentacles?", "answer": "Squid"},
        {"question": "Which animal is known for being slow?", "answer": "Sloth"},
        {"question": "Which bird swims but doesn't fly?", "answer": "Penguin"},
        {"question": "Which animal has tusks and is hunted for ivory?", "answer": "Elephant"},
        {"question": "Which fish can inflate its body?", "answer": "Pufferfish"},
        {"question": "Which bird can fly backward?", "answer": "Hummingbird"},
        {"question": "Which amphibian has poison skin?", "answer": "Poison Dart Frog"},
        {"question": "Which bird sleeps while flying?", "answer": "Albatross"},
        {"question": "Which marine mammal sings underwater?", "answer": "Whale"},
        {"question": "Which desert animal is active only at night?", "answer": "Fennec Fox"},
        {"question": "Which animal has the strongest bite?", "answer": "Crocodile"},
        {"question": "Which reptile has a shell and moves very slowly?", "answer": "Tortoise"},
        {"question": "Which insect glows at night?", "answer": "Firefly"}
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