import streamlit as st 
import os
import time
from dotenv import load_dotenv
import json
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Define system prompts for each persona
system_prompts = {
    "professional": "You are a professional assistant. Respond in a formal, business-like tone.",
    "creative": "You are a creative companion who loves imagination and storytelling.",
    "technical": "You are a technical expert who gives detailed and precise explanations."
}

# Streamlit UI setup
st.title("Conversational LLM Interface")
mode = st.sidebar.selectbox("Choose a persona:", list(system_prompts.keys()))
system_prompt = system_prompts[mode]

# Initialize or update session state
if "mode" not in st.session_state:
    st.session_state.mode = mode
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]

# If user changes persona, reset chat for new mode
if st.session_state.mode != mode:
    st.session_state.mode = mode
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.info(f"Persona changed to **{mode}**. Starting a new conversation.")

# Display chat history
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.text_input("You:")

# Send message
if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write(reply)
    except Exception as e:
        st.error(f"Error: {e}")

# Save chat
if st.button("Save Chat"):
    os.makedirs("data", exist_ok=True)
    filename = f"data/chat_history_{mode}_{int(time.time())}.json"
    with open(filename, "w") as f:
        json.dump({
            "mode": mode,
            "system_prompt": system_prompt,
            "messages": st.session_state.messages
        }, f, indent=4)
    st.success(f"Chat history saved as {filename}")
