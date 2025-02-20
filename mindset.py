import streamlit as st
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", layout='wide')
st.title('🌱 Growth Mindset Challenge')
st.write("Welcome! Track your progress and embrace challenges with a growth mindset.")

# Sidebar for user details
st.sidebar.header("👤 Your Profile")
name = st.sidebar.text_input("Enter your name:")
current_date = datetime.today().strftime('%Y-%m-%d')

# Challenge of the Day
st.subheader("🚀 Challenge of the Day")
challenge_list = [
    "Try learning something completely new today!",
    "Embrace failure and reflect on what you can learn from it.",
    "Step outside your comfort zone and tackle a difficult task.",
    "Ask for constructive feedback and act on it.",
    "Teach someone else a concept you're mastering."
]
selected_challenge = st.selectbox("Choose a challenge to focus on today:", challenge_list)

# Progress Tracker
st.subheader("📊 Track Your Progress")
progress_options = ["Not Started", "In Progress", "Completed"]
progress = st.radio("How far along are you?", progress_options, index=0)

# Reflection Section
st.subheader("✍️ Reflection Journal")
reflection = st.text_area("Write about your experience today:")

# Save Progress (Simulated Data Saving)
if st.button("Save Progress"):
    data = pd.DataFrame({
        "Name": [name],
        "Date": [current_date],
        "Challenge": [selected_challenge],
        "Progress": [progress],
        "Reflection": [reflection]
    })
    st.success("✅ Your progress has been saved! Keep growing!")
    st.dataframe(data)  # Display saved entry

st.sidebar.write("💡 Remember: Growth happens when you push yourself beyond your limits!")
