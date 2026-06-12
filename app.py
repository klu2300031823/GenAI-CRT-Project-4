import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Call Center Supervisor Assistant",
    layout="wide"
)

# Gemini Setup
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📞 Multi-Domain Call Center Supervisor Assistant")

mode = st.sidebar.radio(
    "Choose Mode",
    ["Call Transcript Analysis", "Live Customer Interaction"]
)

# ----------------------------
# TRANSCRIPT MODE
# ----------------------------

if mode == "Call Transcript Analysis":

    st.header("📄 Call Transcript Analysis")

    transcript = st.text_area(
        "Paste Transcript",
        height=300
    )

    if st.button("Analyze Transcript"):

        if transcript.strip() == "":
            st.warning("Please enter transcript.")
            st.stop()

        prompt = f"""
You are an expert Call Center Supervisor Assistant.

Analyze the following conversation and generate:

1. Executive Summary
2. Department
3. Customer Intent
4. Issue Category
5. Customer Sentiment
6. Priority (Low/Medium/High)
7. Resolution Status
8. Agent Performance Review
9. Risk Assessment
10. Next Best Actions
11. Supervisor Recommendation

Conversation:

{transcript}

Format professionally.
"""

        with st.spinner("Analyzing..."):
            response = model.generate_content(prompt)

        st.markdown(response.text)

# ----------------------------
# LIVE INTERACTION MODE
# ----------------------------

else:

    st.header("💬 Live Customer Interaction")

    department = st.selectbox(
        "Select Department",
        [
            "University Admissions",
            "Loan Services",
            "Survey & Feedback",
            "Election Information",
            "Healthcare Support"
        ]
    )

    department_prompt = {
        "University Admissions":
        """
You are a university admissions call center agent.
Help with admissions, eligibility, fees, courses, deadlines.
""",

        "Loan Services":
        """
You are a banking and loan support call center agent.
Help with loans, EMI, applications, eligibility, documents.
""",

        "Survey & Feedback":
        """
You are a survey and feedback support executive.
Collect feedback and answer survey-related questions.
""",

        "Election Information":
        """
You are an election information call center agent.
Provide only official election information.
Do NOT predict winners or provide political advice.
""",

        "Healthcare Support":
        """
You are a healthcare support call center agent.
Provide general health guidance only.
Do NOT diagnose diseases.
Encourage consulting healthcare professionals.
"""
    }

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "conversation_text" not in st.session_state:
        st.session_state.conversation_text = ""

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type your message")

    if user_input:

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        st.session_state.conversation_text += f"\nCustomer: {user_input}"

        with st.chat_message("user"):
            st.markdown(user_input)

        prompt = f"""
{department_prompt[department]}

Customer Message:
{user_input}

Respond like a professional call center agent.
Keep response concise.
"""

        response = model.generate_content(prompt)

        bot_reply = response.text

        st.session_state.messages.append(
            {"role": "assistant", "content": bot_reply}
        )

        st.session_state.conversation_text += f"\nAgent: {bot_reply}"

        with st.chat_message("assistant"):
            st.markdown(bot_reply)

    st.divider()

    if st.button("📊 End Call & Generate Supervisor Report"):

        if st.session_state.conversation_text.strip() == "":
            st.warning("No conversation available.")
            st.stop()

        analysis_prompt = f"""
You are an expert Call Center Supervisor Assistant.

Analyze the complete conversation.

Department:
{department}

Conversation:
{st.session_state.conversation_text}

Generate:

1. Executive Summary
2. Customer Intent
3. Issue Category
4. Sentiment Analysis
5. Priority
6. Resolution Status
7. Agent Performance Review
8. Risk Assessment
9. Next Best Actions
10. Supervisor Recommendation
11. Compliance Check

Provide detailed professional analysis.
"""

        with st.spinner("Generating Supervisor Report..."):
            report = model.generate_content(analysis_prompt)

        st.subheader("📋 Supervisor Analysis Report")
        st.markdown(report.text)

        feedback = st.radio(
            "Was the analysis useful?",
            ["👍 Yes", "👎 No"],
            key="feedback"
        )

        if feedback:
            st.success("Feedback Recorded")
