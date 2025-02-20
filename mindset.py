import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="🌱 Growth Mindset Challenge", layout='wide')
st.title('🌱 Growth Mindset Challenge')
st.write("Welcome! Track your progress and embrace challenges with a growth mindset.")

# Sidebar for user details
st.sidebar.header("👤 Your Profile")
name = st.sidebar.text_input("Enter your name:")
current_date = datetime.today().strftime('%Y-%m-%d')

# Motivational Quote Section
quotes = [
    "“Success is not an accident, success is a choice.” – Stephen Curry",
    "“Failure is success in progress.” – Albert Einstein",
    "“The only way to do great work is to love what you do.” – Steve Jobs",
    "“Don’t let what you cannot do interfere with what you can do.” – John Wooden",
    "“Challenges are what make life interesting. Overcoming them is what makes life meaningful.”"
]
st.sidebar.write("💡 **Motivational Quote:**")
st.sidebar.write(f"📢 *{random.choice(quotes)}*")

# Challenge of the Day
st.subheader("🚀 Challenge of the Day")
challenge_list = [
    "Try learning something completely new today!",
    "Embrace failure and reflect on what you can learn from it.",
    "Step outside your comfort zone and tackle a difficult task.",
    "Ask for constructive feedback and act on it.",
    "Teach someone else a concept you're mastering.",
    "Turn a negative thought into a positive one!",
    "Practice gratitude by writing three things you’re grateful for."
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
if st.button("💾 Save Progress"):
    data = pd.DataFrame({
        "Name": [name if name else "Anonymous"],
        "Date": [current_date],
        "Challenge": [selected_challenge],
        "Progress": [progress],
        "Reflection": [reflection if reflection else "No reflection provided."]
    })
    st.success("✅ Your progress has been saved! Keep growing!")
    st.dataframe(data)

    # Download Progress Data
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Your Progress",
        data=csv,
        file_name=f"growth_mindset_{name}_{current_date}.csv",
        mime="text/csv",
    )

# Progress Visualization
st.subheader("📈 Growth Mindset Progress Chart")
progress_chart_data = pd.DataFrame(
    {"Stage": ["Not Started", "In Progress", "Completed"], "Count": [2, 4, 6]}
)
st.bar_chart(progress_chart_data)


# Dark Mode Toggle
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        body { background-color: #1E1E1E; color: white; }
        .stTextInput, .stTextArea, .stSelectbox, .stRadio { background-color: #333333; color: white; }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.write("💡 Remember: Growth happens when you push yourself beyond your limits!")
