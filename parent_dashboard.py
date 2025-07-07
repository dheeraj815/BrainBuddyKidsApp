import streamlit as st
import pandas as pd


def show_parent_dashboard():
    st.title("👩‍👦 Parent Dashboard - BrainBuddy Kids App")

    if 'quiz_history' not in st.session_state:
        st.session_state.quiz_history = []

    st.subheader("📊 Quiz Attempt History")

    if st.session_state.quiz_history:
        # Convert history list to DataFrame
        data = {
            "Attempt No.": [],
            "Quiz Type": [],
            "Score": [],
            "Total Questions": [],
            "Time": []
        }

        for idx, entry in enumerate(st.session_state.quiz_history):
            data["Attempt No."].append(idx + 1)
            data["Quiz Type"].append(entry['quiz'])
            data["Score"].append(entry['score'])
            data["Total Questions"].append(entry['total'])
            data["Time"].append(entry['time'])

        df = pd.DataFrame(data)

        st.table(df)

        if st.button("🗑️ Clear Entire History"):
            st.session_state.quiz_history = []
            st.success("✅ Quiz history cleared successfully!")

    else:
        st.info("No quiz history available yet.") 