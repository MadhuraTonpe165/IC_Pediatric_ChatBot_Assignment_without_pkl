# -*- coding: utf-8 -*-
"""app.py"""

import streamlit as st
import openai
from chatbot_ped import system_prompt, add_message, get_response

st.set_page_config(page_title="Pediatrician Chatbot", page_icon="🧸")

st.title("🧸 Pediatrician Chatbot")
st.markdown("Your friendly assistant specialized in **pre-teens, teens, child abuse, and children's developmental issues**.")

# --- API Key Input ---
api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")

if api_key:
    openai.api_key = api_key

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = [system_prompt()]

    # Display past messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User input
    if prompt := st.chat_input("Ask me anything..."):
        add_message(st.session_state.messages, "user", prompt)
        with st.chat_message("user"):
            st.write(prompt)

        try:
            reply = get_response(st.session_state.messages)
            with st.chat_message("assistant"):
                st.write(reply)

            add_message(st.session_state.messages, "assistant", reply)

        except Exception as e:
            st.error(f"Error: {e}")

    # Button to clear chat
    if st.button("🔄 Clear Chat"):
        st.session_state.messages = [system_prompt()]
        st.experimental_rerun()
else:
    st.warning("⚠️ Please enter your OpenAI API key to start chatting.")
