# import streamlit as st
# import google.generativeai as genai

# st.set_page_config(
#     page_title="Call Center Supervisor Assistant",
#     layout="wide"
# )

# # Gemini Setup
# genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
# model = genai.GenerativeModel("gemini-2.5-flash")

# st.title("📞 Multi-Domain Call Center Supervisor Assistant")

# mode = st.sidebar.radio(
#     "Choose Mode",
#     ["Call Transcript Analysis", "Live Customer Interaction"]
# )

# # ----------------------------
# # TRANSCRIPT MODE
# # ----------------------------

# if mode == "Call Transcript Analysis":

#     st.header("📄 Call Transcript Analysis")

#     transcript = st.text_area(
#         "Paste Transcript",
#         height=300
#     )

#     if st.button("Analyze Transcript"):

#         if transcript.strip() == "":
#             st.warning("Please enter transcript.")
#             st.stop()

# #         prompt = f"""
# # You are an expert Call Center Supervisor Assistant.

# # Analyze the following conversation and generate:

# # 1. Executive Summary
# # 2. Department
# # 3. Customer Intent
# # 4. Issue Category
# # 5. Customer Sentiment
# # 6. Priority (Low/Medium/High)
# # 7. Resolution Status
# # 8. Agent Performance Review
# # 9. Risk Assessment
# # 10. Next Best Actions
# # 11. Supervisor Recommendation

# # Conversation:

# # {transcript}

# # Format professionally.
# # """

#         prompt = f"""
# {department_prompt[department]}

# Customer Message:
# {user_input}

# Respond as an experienced call center executive.

# You may:
# - Analyze
# - Explain
# - Estimate
# - Predict likely outcomes
# - Provide confidence levels

# Do not guarantee outcomes.

# Keep responses professional and conversational.
# """

#         with st.spinner("Analyzing..."):
#             response = model.generate_content(prompt)

#         st.markdown(response.text)

# # ----------------------------
# # LIVE INTERACTION MODE
# # ----------------------------

# else:

#     st.header("💬 Live Customer Interaction")

#     department = st.selectbox(
#         "Select Department",
#         [
#             "University Admissions",
#             "Loan Services",
#             "Survey & Feedback",
#             "Election Information",
#             "Healthcare Support"
#         ]
#     )

# #     department_prompt = {
# #         "University Admissions":
# #         """
# # You are a university admissions call center agent.
# # Help with admissions, eligibility, fees, courses, deadlines.
# # """,

# #         "Loan Services":
# #         """
# # You are a banking and loan support call center agent.
# # Help with loans, EMI, applications, eligibility, documents.
# # """,

# #         "Survey & Feedback":
# #         """
# # You are a survey and feedback support executive.
# # Collect feedback and answer survey-related questions.
# # """,

# #         "Election Information":
# #         """
# # You are an election information call center agent.
# # Provide only official election information.
# # Do NOT predict winners or provide political advice.
# # """,

# #         "Healthcare Support":
# #         """
# # You are a healthcare support call center agent.
# # Provide general health guidance only.
# # Do NOT diagnose diseases.
# # Encourage consulting healthcare professionals.
# # """
# #     }

#     department_prompt = {

#     "University Admissions":
#     """
# You are a professional university admissions call center executive.

# You help students with:
# - Admission chances
# - Eligibility analysis
# - Cutoff trends
# - Scholarship opportunities
# - Course selection
# - Career guidance
# - Application deadlines

# You may provide estimated chances and recommendations based on information provided by the customer.

# Never guarantee admission.

# Always explain assumptions and limitations.
# """,

#     "Loan Services":
#     """
# You are a professional banking and loan support executive.

# You help customers with:
# - Home loans
# - Education loans
# - Personal loans
# - EMI estimates
# - Eligibility analysis
# - Documentation review
# - Approval likelihood

# You may provide estimated approval probabilities and financial insights.

# Never guarantee loan approval.

# Explain factors affecting decisions.
# """,

#     "Survey & Feedback":
#     """
# You are a survey analytics and feedback specialist.

# You help with:
# - Survey interpretation
# - Customer satisfaction analysis
# - Trend identification
# - Statistical summaries
# - Feedback insights

# You may provide observations, trends and recommendations based on supplied survey data.
# """,

#     "Election Information":
#     """
# You are an election analytics call center specialist.

# You help with:
# - Election information
# - Poll analysis
# - Vote share interpretation
# - Election trends
# - Historical comparisons

# You may discuss likely scenarios and estimated outcomes based on user-provided polling or survey data.

# Never claim certainty.

# Always mention uncertainty, polling limitations and changing voter behavior.
# """,

#     "Healthcare Support":
#     """
# You are a healthcare support specialist.

# You help with:
# - Symptom interpretation
# - General health guidance
# - Wellness information
# - Preventive care

# You may discuss possible conditions based on reported symptoms.

# Do not claim a definite diagnosis.

# Recommend professional medical evaluation when appropriate.
# """
# }

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     if "conversation_text" not in st.session_state:
#         st.session_state.conversation_text = ""

#     # Display chat history
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     user_input = st.chat_input("Type your message")

#     if user_input:

#         st.session_state.messages.append(
#             {"role": "user", "content": user_input}
#         )

#         st.session_state.conversation_text += f"\nCustomer: {user_input}"

#         with st.chat_message("user"):
#             st.markdown(user_input)

#         prompt = f"""
# {department_prompt[department]}

# Customer Message:
# {user_input}

# Respond like a professional call center agent.
# Keep response concise.
# """

#         response = model.generate_content(prompt)

#         bot_reply = response.text

#         st.session_state.messages.append(
#             {"role": "assistant", "content": bot_reply}
#         )

#         st.session_state.conversation_text += f"\nAgent: {bot_reply}"

#         with st.chat_message("assistant"):
#             st.markdown(bot_reply)

#     st.divider()

#     if st.button("📊 End Call & Generate Supervisor Report"):

#         if st.session_state.conversation_text.strip() == "":
#             st.warning("No conversation available.")
#             st.stop()

#         analysis_prompt = f"""
# You are an expert Call Center Supervisor Assistant.

# Analyze the complete conversation.

# Department:
# {department}

# Conversation:
# {st.session_state.conversation_text}

# Generate:

# 1. Executive Summary
# 2. Customer Intent
# 3. Issue Category
# 4. Sentiment Analysis
# 5. Priority
# 6. Resolution Status
# 7. Agent Performance Review
# 8. Risk Assessment
# 9. Next Best Actions
# 10. Supervisor Recommendation
# 11. Compliance Check

# Provide detailed professional analysis.
# """

#         with st.spinner("Generating Supervisor Report..."):
#             report = model.generate_content(analysis_prompt)

#         st.subheader("📋 Supervisor Analysis Report")
#         st.markdown(report.text)

#         feedback = st.radio(
#             "Was the analysis useful?",
#             ["👍 Yes", "👎 No"],
#             key="feedback"
#         )

#         if feedback:
#             st.success("Feedback Recorded")


#```python
import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Call Center Supervisor Assistant",
    layout="wide"
)

# -----------------------
# GEMINI SETUP
# -----------------------

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------
# DOMAIN PROMPTS
# -----------------------

department_prompt = {

    "University Admissions": """
You are a professional university admissions call center executive.

Help with:
- Admission chances
- Eligibility
- Scholarships
- Course selection
- Cutoff trends
- Career guidance

You may provide estimated chances and recommendations.

Never guarantee admission.
Always mention assumptions.
""",

    "Loan Services": """
You are a professional loan support executive.

Help with:
- Home loans
- Education loans
- EMI calculations
- Eligibility analysis
- Documentation review
- Approval likelihood

You may provide estimated approval probabilities.

Never guarantee loan approval.
""",

    "Survey & Feedback": """
You are a survey analytics specialist.

Help with:
- Survey interpretation
- Feedback analysis
- Trend identification
- Statistical summaries

Provide insights and recommendations.
""",

    "Election Information": """
You are an election analytics specialist.

Help with:
- Poll analysis
- Vote share interpretation
- Election trends
- Historical comparisons

You may discuss likely scenarios and estimates.

Never claim certainty.
Always mention uncertainty and limitations.
""",

    "Healthcare Support": """
You are a healthcare support specialist.

Help with:
- Symptom interpretation
- Health guidance
- Wellness information
- Preventive care

You may discuss possible conditions.

Do not claim a definite diagnosis.
Recommend medical consultation when appropriate.
"""
}

# -----------------------
# TITLE
# -----------------------

st.title("📞 AI Call Center Supervisor Assistant")

mode = st.sidebar.radio(
    "Choose Mode",
    [
        "Call Transcript Analysis",
        "Live Customer Interaction"
    ]
)

# =====================================================
# TRANSCRIPT ANALYSIS
# =====================================================

if mode == "Call Transcript Analysis":

    st.header("📄 Call Transcript Analysis")

    transcript = st.text_area(
        "Paste Transcript",
        height=350
    )

    if st.button("Analyze Transcript"):

        if not transcript.strip():
            st.warning("Please enter transcript.")
            st.stop()

        prompt = f"""
You are an expert Call Center Supervisor Assistant.

Analyze the following transcript.

Generate:

# Executive Summary

# Department
(Identify automatically)

# Customer Intent

# Issue Category

# Key Facts Identified

# Customer Sentiment

# Priority

# Resolution Status

# Agent Performance Review

# Risk Assessment

# Predicted Outcome
(If applicable)

# Confidence Score (0-100)

# Next Best Actions

# Supervisor Recommendation

# Compliance Check

# Business Impact

Transcript:

{transcript}

Provide a detailed professional report.
"""

        with st.spinner("Analyzing Transcript..."):
            response = model.generate_content(prompt)

        st.markdown(response.text)

# =====================================================
# LIVE CUSTOMER INTERACTION
# =====================================================

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

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "conversation_text" not in st.session_state:
        st.session_state.conversation_text = ""

    col1, col2 = st.columns([1,1])

    with col1:
        if st.button("🆕 Start New Call"):
            st.session_state.messages = []
            st.session_state.conversation_text = ""
            st.rerun()

    with col2:
        st.write(f"**Department:** {department}")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Customer Message")

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        st.session_state.conversation_text += (
            f"\nCustomer: {user_input}"
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        prompt = f"""
{department_prompt[department]}

Customer Message:

{user_input}

Respond like a professional call center executive.

You may:
- Explain
- Analyze
- Estimate
- Predict likely outcomes
- Provide confidence levels

Never guarantee outcomes.

Keep answers concise and conversational.
"""

        with st.spinner("Agent Responding..."):
            response = model.generate_content(prompt)

        bot_reply = response.text

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_reply
            }
        )

        st.session_state.conversation_text += (
            f"\nAgent: {bot_reply}"
        )

        with st.chat_message("assistant"):
            st.markdown(bot_reply)

    st.divider()

    if st.button("📊 End Call & Generate Supervisor Report"):

        if not st.session_state.conversation_text.strip():
            st.warning("No conversation available.")
            st.stop()

        analysis_prompt = f"""
You are an expert Call Center Supervisor Assistant.

Analyze the complete call.

Department:
{department}

Conversation:
{st.session_state.conversation_text}

Generate:

# Executive Summary

# Customer Intent

# Issue Category

# Key Facts Identified

# Customer Sentiment

# Priority

# Resolution Status

# Agent Performance Review

# Risk Assessment

# Predicted Outcome
(If applicable)

# Confidence Score (0-100)

# Next Best Actions

# Supervisor Recommendation

# Compliance Check

# Business Impact

Provide a detailed professional supervisor report.
"""

        with st.spinner("Generating Supervisor Report..."):
            report = model.generate_content(
                analysis_prompt
            )

        st.subheader("📋 Supervisor Analysis Report")

        st.markdown(report.text)

        feedback = st.radio(
            "Was this report useful?",
            ["👍 Yes", "👎 No"],
            key="feedback"
        )

        if feedback:
            st.success("Feedback Recorded")
#```

