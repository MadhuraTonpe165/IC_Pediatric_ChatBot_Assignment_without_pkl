# -*- coding: utf-8 -*-
"""app.py"""

import streamlit as st
import openai
import pickle
from chatbot_ped import PediatricChatbot

st.set_page_config(page_title="Pediatrician Chatbot", page_icon="🧸")

st.title("🧸 Pediatrician Chatbot")
st.markdown("Your friendly assistant specialized in **pre-teens, teens, child abuse, and children's developmental issues**.")

# --- API Key Input ---
api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")

if api_key:
    openai.api_key = api_key

    # Load chatbot from pickle (once)
    if "chatbot" not in st.session_state:
        with open("Pedictric_Help_bot.pkl", "rb") as f:
            st.session_state.chatbot = pickle.load(f)

    chatbot = st.session_state.chatbot

    # Display past messages
    for msg in chatbot.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User input
    if prompt := st.chat_input("Ask me anything..."):
        chatbot.add_message("user", prompt)
        with st.chat_message("user"):
            st.write(prompt)

        try:
            reply = chatbot.get_response()
            with st.chat_message("assistant"):
                st.write(reply)

        except Exception as e:
            st.error(f"Error: {e}")

    # Button to clear chat
    if st.button("🔄 Clear Chat"):
        chatbot.messages = [chatbot.messages[0]]  # reset with only system prompt
        st.experimental_rerun()
else:
    st.warning("⚠️ Please enter your OpenAI API key to start chatting.")
