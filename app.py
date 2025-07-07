import streamlit as st
import math_quiz
import vocabulary
import riddles
import fun_facts
import animal_quiz
import parent_dashboard

st.set_page_config(page_title="BrainBuddy Kids App 🎈", layout="centered")

st.title("BrainBuddy Kids App 🎈")

st.sidebar.title("📋 Navigation")
page = st.sidebar.selectbox("Select Activity", [
    "Home",
    "Math Quiz",
    "Vocabulary Quiz",
    "Riddles",
    "Fun Facts",
    "Animal Quiz",
    "Parent Dashboard"
])

if page == "Home":
    st.header("Welcome to BrainBuddy Kids App!")
    st.markdown("""
    👉 Choose an activity from the left sidebar:

    - Math Quiz  
    - Vocabulary Quiz  
    - Riddles  
    - Fun Facts  
    - Animal Quiz  
    - Parent Dashboard (For Parents)  

    ✅ Have fun learning!
    """)
elif page == "Math Quiz":
    math_quiz.run_math_quiz()
elif page == "Vocabulary Quiz":
    vocabulary.run_vocabulary_quiz()
elif page == "Riddles":
    riddles.run_riddles()
elif page == "Fun Facts":
    fun_facts.run_fun_facts_quiz()
elif page == "Animal Quiz":
    animal_quiz.run_animal_quiz()
elif page == "Parent Dashboard":
    parent_dashboard.show_parent_dashboard()