import streamlit as st
from agent.hospital import create_agent

st.set_page_config(
    page_title="Hospital Service AI Assistant",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Hospital Service AI Assistant")
st.caption("Welcome! This assistant provides non-medical hospital service information.")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask about registration, doctor schedules, visiting hours...")

if user_input:
    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Agent response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.run(user_input)
            st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
    
#Author: Natalia Reta Budiarti