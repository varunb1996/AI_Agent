import streamlit as st
from main_agent import run_agent_task

st.title("🤖 AutoPro: Autonomous AI Agent")
user_task = st.text_input("What do you want the AI Agent to do?")
if st.button("Run"):
    output = run_agent_task(user_task)
    st.write(output)