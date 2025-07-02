import streamlit as st
import datetime
from logic.input_processing import validate_inputs

st.set_page_config(page_title="Study Plan Recommender", layout="centered")
st.title("📚 AI-Powered Study Plan Recommender")
st.subheader("Enter Your Study Preferences")

subjects = st.text_input("Enter subjects (comma-separated)", "Math, Physics, DSA")
subject_list = [s.strip() for s in subjects.split(',') if s.strip()]

study_hours = st.slider("How many hours can you study per day?", 1, 12, 4)
target_date = st.date_input("Target completion date", datetime.date(2025, 7, 30))
weak_subjects = st.multiselect("Select weak subjects to prioritize", subject_list)
days_off = st.multiselect("Preferred days off", ["Monday", "Tuesday", "Wednesday", 
                                                  "Thursday", "Friday", "Saturday", "Sunday"])

if st.button("Submit"):
    errors = validate_inputs(subject_list, study_hours, target_date)
    if errors:
        st.error(" | ".join(errors))
    else:
        st.success("Inputs collected successfully!")
        st.write("Subjects:", subject_list)
        st.write("Study Hours/Day:", study_hours)
        st.write("Target Date:", target_date)
        st.write("Priority Subjects:", weak_subjects)
        st.write("Days Off:", days_off)
