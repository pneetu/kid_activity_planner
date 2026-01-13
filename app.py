# app.py
import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Kid-Friendly Activity Planner", page_icon="🎃")
# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title(" Kid-Friendly Activity Planner")

# Inputs
date = st.date_input("Select a date")
location = st.text_input("Enter location")

if st.button("Find Activities"):
    activities = run_agent(str(date), location)
    
    if not activities:
        st.warning("No activities found for this date/location!")
    else:
        st.success(f"Found {len(activities)} activities:")
        for act in activities:
            st.write(f"**{act['name']}** at {act['location']} ({act['date']})")
