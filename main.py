import streamlit as st
import datetime
import pandas as pd
from logic.input_processing import validate_inputs
from logic.scheduler import generate_schedule
from logic.optimizer import optimize_schedule
from logic.exporter import export_schedule

st.set_page_config(page_title="AI Study Planner", layout="centered")
st.title("📚 AI-Powered Study Plan Recommender")
st.subheader("Enter Your Study Preferences")

subjects = st.text_input("Enter subjects (comma-separated)", "Math, Physics, DSA")
subject_list = [s.strip() for s in subjects.split(',') if s.strip()]
study_hours = st.slider("Study hours per day", 1, 12, 4)
target_date = st.date_input("Target Completion Date", datetime.date(2025, 7, 30))
weak_subjects = st.multiselect("Weak subjects to prioritize", subject_list)
days_off = st.multiselect("Preferred days off", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
num_breaks = st.slider("Number of breaks per day", 0, 5, 1)
break_duration = st.slider("Break duration (in minutes)", 10, 60, 15)
start_hour = st.slider("Daily start time (in 24hrs format)", 5, 18, 5)


if st.button("Generate Study Plan"):
    errors = validate_inputs(subject_list, study_hours, target_date)
    if errors:
        st.error(" | ".join(errors))
    else:
        st.success("✅ Inputs are valid. Proceeding with scheduling...")

        raw_schedule = generate_schedule(subject_list, study_hours, target_date,weak_subjects, days_off, num_breaks, break_duration,start_hour)
        st.subheader("Schedule")
        st.dataframe(raw_schedule)

        # st.subheader("Phase 3: Optimized Schedule")
        # optimized = optimize_schedule(raw_schedule, weak_subjects)
        # st.dataframe(optimized)

        st.subheader("Download Your Plan")
        export_schedule(raw_schedule)
