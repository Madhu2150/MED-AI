import streamlit as st
import model

st.set_page_config(page_title="MEDIAI — Assistant", page_icon="💬", layout="wide")

# Sidebar
with st.sidebar:
    st.markdown("### 💬 Medical Assistant")
    st.markdown("Ask about symptoms, conditions, treatments.")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages_chatbot_1 = []
        st.rerun()
    st.markdown("---")
    st.caption("Model: Gemini 1.5 Flash · Temp: 0.4")

st.markdown("## 💬 Medical Assistant")
st.caption("Describe your symptoms below — MEDIAI will help.")

if "messages_chatbot_1" not in st.session_state:
    st.session_state.messages_chatbot_1 = []

for message in st.session_state.messages_chatbot_1:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Describe symptoms or ask a medical question..."):
    st.session_state.messages_chatbot_1.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🧠"):
            response = model.model(prompt, history=st.session_state.messages_chatbot_1)
            st.markdown(response)
    st.session_state.messages_chatbot_1.append({"role": "assistant", "content": response})