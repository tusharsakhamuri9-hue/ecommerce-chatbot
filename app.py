import streamlit as st
from chatbot import process_query

st.set_page_config(
    page_title="E-Commerce Chatbot",
    page_icon="🛒"
)

st.title("🛒 E-Commerce Shopping Assistant")

# Conversation History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
user_input = st.chat_input(
    "Ask about products, comparisons, or order tracking..."
)

if user_input:

    # Show User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Spinner
    with st.spinner("Thinking..."):

        response = process_query(user_input)

    # Show Bot Response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )