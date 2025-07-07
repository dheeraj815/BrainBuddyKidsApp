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
        {"question": "What is the smallest planet in our solar system?", "answer": "Mercury"},
        {"question": "What gas do plants absorb?", "answer": "Carbon dioxide"},
        {"question": "How many continents are there on Earth?", "answer": "7"},
        {"question": "Which is the largest ocean on Earth?", "answer": "Pacific Ocean"},
        {"question": "Which is the longest river in the world?", "answer": "Nile"},
        {"question": "Which bird lays the largest eggs?", "answer": "Ostrich"},
        {"question": "What is the capital of India?", "answer": "New Delhi"},
        {"question": "Which is the only planet that supports life?", "answer": "Earth"},
        {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
        {"question": "Which planet is closest to the Sun?", "answer": "Mercury"},
        {"question": "What is H2O commonly known as?", "answer": "Water"},
        {"question": "Which animal is known for changing colors?", "answer": "Chameleon"},
        {"question": "What is the largest desert in the world?", "answer": "Sahara"},
        {"question": "How many teeth does an adult human have?", "answer": "32"},
        {"question": "What is the fastest bird in the world?", "answer": "Peregrine Falcon"},
        {"question": "Which planet is called the Morning Star?", "answer": "Venus"},
        {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
        {"question": "Which ocean is the smallest?", "answer": "Arctic Ocean"},
        {"question": "Which organ pumps blood in the human body?", "answer": "Heart"},
        {"question": "What is the largest continent?", "answer": "Asia"},
        {"question": "Which animal is known as man's best friend?", "answer": "Dog"},
        {"question": "What do bees produce?", "answer": "Honey"},
        {"question": "Which gas is most abundant in Earth's atmosphere?", "answer": "Nitrogen"},
        {"question": "What is the main source of energy for Earth?", "answer": "The Sun"},
        {"question": "Which animal is known for its black and white stripes?", "answer": "Zebra"},
        {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
        {"question": "How many planets are in our solar system?", "answer": "8"},
        {"question": "Which metal has the chemical symbol 'Fe'?", "answer": "Iron"},
        {"question": "What is the largest organ in the human body?", "answer": "Skin"},
        {"question": "What is the chemical formula for table salt?", "answer": "NaCl"},
        {"question": "Which bird is a universal symbol of peace?", "answer": "Dove"},
        {"question": "How many sides does a hexagon have?", "answer": "6"},
        {"question": "What is the main ingredient in sushi?", "answer": "Rice"},
        {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
        {"question": "Which planet is known for its Great Red Spot?", "answer": "Jupiter"},
        {"question": "What is the freezing point of water in Celsius?", "answer": "0"},
        {"question": "Which animal is the largest land carnivore?", "answer": "Polar Bear"},
        {"question": "What is the smallest unit of life?", "answer": "Cell"},
        {"question": "Who developed the theory of relativity?", "answer": "Einstein"},
        {"question": "Which instrument is used to measure temperature?", "answer": "Thermometer"},
        {"question": "What is the currency of the United States?", "answer": "Dollar"}
    ]

   