import streamlit as st
import requests

st.set_page_config(page_title="AI Supervisor Assistant", layout="wide")
st.title("📞 Call-Center Supervisor Assistant")

# -----------------------------
# FREE HUGGINGFACE ENDPOINT
# -----------------------------
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

def query_model(prompt):
    response = requests.post(API_URL, json={"inputs": prompt})
    try:
        return response.json()[0]["generated_text"]
    except:
        return "Model is busy, please try again."

# -----------------------------
# SESSION
# -----------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# -----------------------------
# INPUT
# -----------------------------
user_input = st.chat_input("Enter customer interaction...")

if user_input:
    st.session_state.chat.append(("User", user_input))

    prompt = f"""
    You are a professional call-center assistant.

    Conversation:
    {user_input}

    Ask a smart follow-up question.
    """

    reply = query_model(prompt)
    st.session_state.chat.append(("Assistant", reply))

# -----------------------------
# SHOW CHAT
# -----------------------------
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)

# -----------------------------
# ANALYSIS
# -----------------------------
if st.button("📊 Generate Summary & Action"):

    convo = " ".join([m for _, m in st.session_state.chat])

    prompt = f"""
    Analyze call-center conversation:

    {convo}

    Give:
    1. Summary
    2. Domain (Loan / Admission / Survey / Election / Healthcare)
    3. Next-best-action
    """

    result = query_model(prompt)

    st.subheader("📌 Analysis")
    st.write(result)

# -----------------------------
# RESET
# -----------------------------
if st.button("🔄 Reset"):
    st.session_state.chat = []
    st.rerun()
