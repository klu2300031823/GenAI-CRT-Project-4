# # # # import streamlit as st
# # # # import google.generativeai as genai

# # # # st.set_page_config(
# # # #     page_title="Call Center Supervisor Assistant",
# # # #     layout="wide"
# # # # )

# # # # # Gemini Setup
# # # # genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
# # # # model = genai.GenerativeModel("gemini-2.5-flash")

# # # # st.title(" Multi-Domain Call Center Supervisor Assistant")

# # # # mode = st.sidebar.radio(
# # # #     "Choose Mode",
# # # #     ["Call Transcript Analysis", "Live Customer Interaction"]
# # # # )

# # # # # ----------------------------
# # # # # TRANSCRIPT MODE
# # # # # ----------------------------

# # # # if mode == "Call Transcript Analysis":

# # # #     st.header(" Call Transcript Analysis")

# # # #     transcript = st.text_area(
# # # #         "Paste Transcript",
# # # #         height=300
# # # #     )

# # # #     if st.button("Analyze Transcript"):

# # # #         if transcript.strip() == "":
# # # #             st.warning("Please enter transcript.")
# # # #             st.stop()

# # # # #         prompt = f"""
# # # # # You are an expert Call Center Supervisor Assistant.

# # # # # Analyze the following conversation and generate:

# # # # # 1. Executive Summary
# # # # # 2. Department
# # # # # 3. Customer Intent
# # # # # 4. Issue Category
# # # # # 5. Customer Sentiment
# # # # # 6. Priority (Low/Medium/High)
# # # # # 7. Resolution Status
# # # # # 8. Agent Performance Review
# # # # # 9. Risk Assessment
# # # # # 10. Next Best Actions
# # # # # 11. Supervisor Recommendation

# # # # # Conversation:

# # # # # {transcript}

# # # # # Format professionally.
# # # # # """

# # # #         prompt = f"""
# # # # {department_prompt[department]}

# # # # Customer Message:
# # # # {user_input}

# # # # Respond as an experienced call center executive.

# # # # You may:
# # # # - Analyze
# # # # - Explain
# # # # - Estimate
# # # # - Predict likely outcomes
# # # # - Provide confidence levels

# # # # Do not guarantee outcomes.

# # # # Keep responses professional and conversational.
# # # # """

# # # #         with st.spinner("Analyzing..."):
# # # #             response = model.generate_content(prompt)

# # # #         st.markdown(response.text)

# # # # # ----------------------------
# # # # # LIVE INTERACTION MODE
# # # # # ----------------------------

# # # # else:

# # # #     st.header(" Live Customer Interaction")

# # # #     department = st.selectbox(
# # # #         "Select Department",
# # # #         [
# # # #             "University Admissions",
# # # #             "Loan Services",
# # # #             "Survey & Feedback",
# # # #             "Election Information",
# # # #             "Healthcare Support"
# # # #         ]
# # # #     )

# # # # #     department_prompt = {
# # # # #         "University Admissions":
# # # # #         """
# # # # # You are a university admissions call center agent.
# # # # # Help with admissions, eligibility, fees, courses, deadlines.
# # # # # """,

# # # # #         "Loan Services":
# # # # #         """
# # # # # You are a banking and loan support call center agent.
# # # # # Help with loans, EMI, applications, eligibility, documents.
# # # # # """,

# # # # #         "Survey & Feedback":
# # # # #         """
# # # # # You are a survey and feedback support executive.
# # # # # Collect feedback and answer survey-related questions.
# # # # # """,

# # # # #         "Election Information":
# # # # #         """
# # # # # You are an election information call center agent.
# # # # # Provide only official election information.
# # # # # Do NOT predict winners or provide political advice.
# # # # # """,

# # # # #         "Healthcare Support":
# # # # #         """
# # # # # You are a healthcare support call center agent.
# # # # # Provide general health guidance only.
# # # # # Do NOT diagnose diseases.
# # # # # Encourage consulting healthcare professionals.
# # # # # """
# # # # #     }

# # # #     department_prompt = {

# # # #     "University Admissions":
# # # #     """
# # # # You are a professional university admissions call center executive.

# # # # You help students with:
# # # # - Admission chances
# # # # - Eligibility analysis
# # # # - Cutoff trends
# # # # - Scholarship opportunities
# # # # - Course selection
# # # # - Career guidance
# # # # - Application deadlines

# # # # You may provide estimated chances and recommendations based on information provided by the customer.

# # # # Never guarantee admission.

# # # # Always explain assumptions and limitations.
# # # # """,

# # # #     "Loan Services":
# # # #     """
# # # # You are a professional banking and loan support executive.

# # # # You help customers with:
# # # # - Home loans
# # # # - Education loans
# # # # - Personal loans
# # # # - EMI estimates
# # # # - Eligibility analysis
# # # # - Documentation review
# # # # - Approval likelihood

# # # # You may provide estimated approval probabilities and financial insights.

# # # # Never guarantee loan approval.

# # # # Explain factors affecting decisions.
# # # # """,

# # # #     "Survey & Feedback":
# # # #     """
# # # # You are a survey analytics and feedback specialist.

# # # # You help with:
# # # # - Survey interpretation
# # # # - Customer satisfaction analysis
# # # # - Trend identification
# # # # - Statistical summaries
# # # # - Feedback insights

# # # # You may provide observations, trends and recommendations based on supplied survey data.
# # # # """,

# # # #     "Election Information":
# # # #     """
# # # # You are an election analytics call center specialist.

# # # # You help with:
# # # # - Election information
# # # # - Poll analysis
# # # # - Vote share interpretation
# # # # - Election trends
# # # # - Historical comparisons

# # # # You may discuss likely scenarios and estimated outcomes based on user-provided polling or survey data.

# # # # Never claim certainty.

# # # # Always mention uncertainty, polling limitations and changing voter behavior.
# # # # """,

# # # #     "Healthcare Support":
# # # #     """
# # # # You are a healthcare support specialist.

# # # # You help with:
# # # # - Symptom interpretation
# # # # - General health guidance
# # # # - Wellness information
# # # # - Preventive care

# # # # You may discuss possible conditions based on reported symptoms.

# # # # Do not claim a definite diagnosis.

# # # # Recommend professional medical evaluation when appropriate.
# # # # """
# # # # }

# # # #     if "messages" not in st.session_state:
# # # #         st.session_state.messages = []

# # # #     if "conversation_text" not in st.session_state:
# # # #         st.session_state.conversation_text = ""

# # # #     # Display chat history
# # # #     for msg in st.session_state.messages:
# # # #         with st.chat_message(msg["role"]):
# # # #             st.markdown(msg["content"])

# # # #     user_input = st.chat_input("Type your message")

# # # #     if user_input:

# # # #         st.session_state.messages.append(
# # # #             {"role": "user", "content": user_input}
# # # #         )

# # # #         st.session_state.conversation_text += f"\nCustomer: {user_input}"

# # # #         with st.chat_message("user"):
# # # #             st.markdown(user_input)

# # # #         prompt = f"""
# # # # {department_prompt[department]}

# # # # Customer Message:
# # # # {user_input}

# # # # Respond like a professional call center agent.
# # # # Keep response concise.
# # # # """

# # # #         response = model.generate_content(prompt)

# # # #         bot_reply = response.text

# # # #         st.session_state.messages.append(
# # # #             {"role": "assistant", "content": bot_reply}
# # # #         )

# # # #         st.session_state.conversation_text += f"\nAgent: {bot_reply}"

# # # #         with st.chat_message("assistant"):
# # # #             st.markdown(bot_reply)

# # # #     st.divider()

# # # #     if st.button(" End Call & Generate Supervisor Report"):

# # # #         if st.session_state.conversation_text.strip() == "":
# # # #             st.warning("No conversation available.")
# # # #             st.stop()

# # # #         analysis_prompt = f"""
# # # # You are an expert Call Center Supervisor Assistant.

# # # # Analyze the complete conversation.

# # # # Department:
# # # # {department}

# # # # Conversation:
# # # # {st.session_state.conversation_text}

# # # # Generate:

# # # # 1. Executive Summary
# # # # 2. Customer Intent
# # # # 3. Issue Category
# # # # 4. Sentiment Analysis
# # # # 5. Priority
# # # # 6. Resolution Status
# # # # 7. Agent Performance Review
# # # # 8. Risk Assessment
# # # # 9. Next Best Actions
# # # # 10. Supervisor Recommendation
# # # # 11. Compliance Check

# # # # Provide detailed professional analysis.
# # # # """

# # # #         with st.spinner("Generating Supervisor Report..."):
# # # #             report = model.generate_content(analysis_prompt)

# # # #         st.subheader(" Supervisor Analysis Report")
# # # #         st.markdown(report.text)

# # # #         feedback = st.radio(
# # # #             "Was the analysis useful?",
# # # #             [" Yes", " No"],
# # # #             key="feedback"
# # # #         )

# # # #         if feedback:
# # # #             st.success("Feedback Recorded")


# # # #```python
# # import streamlit as st
# # import google.generativeai as genai

# # st.set_page_config(
# #     page_title="AI Call Center Supervisor Assistant",
# #     layout="wide"
# # )

# # # -----------------------
# # # GEMINI SETUP
# # # -----------------------

# # genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
# # model = genai.GenerativeModel("gemini-2.5-flash")

# # # -----------------------
# # # DOMAIN PROMPTS
# # # -----------------------

# # department_prompt = {

# #     "University Admissions": """
# # You are a professional university admissions call center executive.

# # Help with:
# # - Admission chances
# # - Eligibility
# # - Scholarships
# # - Course selection
# # - Cutoff trends
# # - Career guidance

# # You may provide estimated chances and recommendations.

# # Never guarantee admission.
# # Always mention assumptions.
# # """,

# #     "Loan Services": """
# # You are a professional loan support executive.

# # Help with:
# # - Home loans
# # - Education loans
# # - EMI calculations
# # - Eligibility analysis
# # - Documentation review
# # - Approval likelihood

# # You may provide estimated approval probabilities.

# # Never guarantee loan approval.
# # """,

# #     "Survey & Feedback": """
# # You are a survey analytics specialist.

# # Help with:
# # - Survey interpretation
# # - Feedback analysis
# # - Trend identification
# # - Statistical summaries

# # Provide insights and recommendations.
# # """,

# #     "Election Information": """
# # You are an election analytics specialist.

# # Help with:
# # - Poll analysis
# # - Vote share interpretation
# # - Election trends
# # - Historical comparisons

# # You may discuss likely scenarios and estimates.

# # Never claim certainty.
# # Always mention uncertainty and limitations.
# # """,

# #     "Healthcare Support": """
# # You are a healthcare support specialist.

# # Help with:
# # - Symptom interpretation
# # - Health guidance
# # - Wellness information
# # - Preventive care

# # You may discuss possible conditions.

# # Do not claim a definite diagnosis.
# # Recommend medical consultation when appropriate.
# # """
# # }

# # # -----------------------
# # # TITLE
# # # -----------------------

# # st.title("📞 AI Call Center Supervisor Assistant")

# # mode = st.sidebar.radio(
# #     "Choose Mode",
# #     [
# #         "Call Transcript Analysis",
# #         "Live Customer Interaction"
# #     ]
# # )

# # # =====================================================
# # # TRANSCRIPT ANALYSIS
# # # =====================================================

# # if mode == "Call Transcript Analysis":

# #     st.header("📄 Call Transcript Analysis")

# #     transcript = st.text_area(
# #         "Paste Transcript",
# #         height=350
# #     )

# #     if st.button("Analyze Transcript"):

# #         if not transcript.strip():
# #             st.warning("Please enter transcript.")
# #             st.stop()

# #         prompt = f"""
# # You are an expert Call Center Supervisor Assistant.

# # Analyze the following transcript.

# # Generate:

# # # Executive Summary

# # # Department
# # (Identify automatically)

# # # Customer Intent

# # # Issue Category

# # # Key Facts Identified

# # # Customer Sentiment

# # # Priority

# # # Resolution Status

# # # Agent Performance Review

# # # Risk Assessment

# # # Predicted Outcome
# # (If applicable)

# # # Confidence Score (0-100)

# # # Next Best Actions

# # # Supervisor Recommendation

# # # Compliance Check

# # # Business Impact

# # Transcript:

# # {transcript}

# # Provide a detailed professional report.
# # """

# #         with st.spinner("Analyzing Transcript..."):
# #             response = model.generate_content(prompt)

# #         st.markdown(response.text)

# # # =====================================================
# # # LIVE CUSTOMER INTERACTION
# # # =====================================================

# # else:

# #     st.header("💬 Live Customer Interaction")

# #     department = st.selectbox(
# #         "Select Department",
# #         [
# #             "University Admissions",
# #             "Loan Services",
# #             "Survey & Feedback",
# #             "Election Information",
# #             "Healthcare Support"
# #         ]
# #     )

# #     if "messages" not in st.session_state:
# #         st.session_state.messages = []

# #     if "conversation_text" not in st.session_state:
# #         st.session_state.conversation_text = ""

# #     col1, col2 = st.columns([1,1])

# #     with col1:
# #         if st.button("🆕 Start New Call"):
# #             st.session_state.messages = []
# #             st.session_state.conversation_text = ""
# #             st.rerun()

# #     with col2:
# #         st.write(f"**Department:** {department}")

# #     for msg in st.session_state.messages:
# #         with st.chat_message(msg["role"]):
# #             st.markdown(msg["content"])

# #     user_input = st.chat_input("Customer Message")

# #     if user_input:

# #         st.session_state.messages.append(
# #             {
# #                 "role": "user",
# #                 "content": user_input
# #             }
# #         )

# #         st.session_state.conversation_text += (
# #             f"\nCustomer: {user_input}"
# #         )

# #         with st.chat_message("user"):
# #             st.markdown(user_input)

# #         prompt = f"""
# # {department_prompt[department]}

# # Customer Message:

# # {user_input}

# # Respond like a professional call center executive.

# # You may:
# # - Explain
# # - Analyze
# # - Estimate
# # - Predict likely outcomes
# # - Provide confidence levels

# # Never guarantee outcomes.

# # Keep answers concise and conversational.
# # """

# #         with st.spinner("Agent Responding..."):
# #             response = model.generate_content(prompt)

# #         bot_reply = response.text

# #         st.session_state.messages.append(
# #             {
# #                 "role": "assistant",
# #                 "content": bot_reply
# #             }
# #         )

# #         st.session_state.conversation_text += (
# #             f"\nAgent: {bot_reply}"
# #         )

# #         with st.chat_message("assistant"):
# #             st.markdown(bot_reply)

# #     st.divider()

# #     if st.button("📊 End Call & Generate Supervisor Report"):

# #         if not st.session_state.conversation_text.strip():
# #             st.warning("No conversation available.")
# #             st.stop()

# #         analysis_prompt = f"""
# # You are an expert Call Center Supervisor Assistant.

# # Analyze the complete call.

# # Department:
# # {department}

# # Conversation:
# # {st.session_state.conversation_text}

# # Generate:

# # # Executive Summary

# # # Customer Intent

# # # Issue Category

# # # Key Facts Identified

# # # Customer Sentiment

# # # Priority

# # # Resolution Status

# # # Agent Performance Review

# # # Risk Assessment

# # # Predicted Outcome
# # (If applicable)

# # # Confidence Score (0-100)

# # # Next Best Actions

# # # Supervisor Recommendation

# # # Compliance Check

# # # Business Impact

# # Provide a detailed professional supervisor report.
# # """

# #         with st.spinner("Generating Supervisor Report..."):
# #             report = model.generate_content(
# #                 analysis_prompt
# #             )

# #         st.subheader("📋 Supervisor Analysis Report")

# #         st.markdown(report.text)

# #         feedback = st.radio(
# #             "Was this report useful?",
# #             ["👍 Yes", "👎 No"],
# #             key="feedback"
# #         )

# #         if feedback:
# #             st.success("Feedback Recorded")
# # #```

# # # import streamlit as st
# # # import google.generativeai as genai

# # # genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# # # try:
# # #     models = genai.list_models()

# # #     for m in models:
# # #         st.write(m.name)

# # # except Exception as e:
# # #     st.error(str(e))
# import streamlit as st

# st.set_page_config(page_title="AI Call Center Assistant", layout="wide")

# st.title("📞 AI Call Center Supervisor Assistant")

# module = st.selectbox(
#     "Select Call Type",
#     ["Loan", "Insurance", "Telecom", "E-Commerce", "General"]
# )

# transcript = st.text_area(
#     "Paste Call Transcript",
#     height=300,
#     placeholder="""Customer: I need a home loan.
# Agent: Sure sir.
# Customer: My salary is 75000.
# Customer: I need 10 lakh loan."""
# )

# if st.button("Analyze"):

#     if not transcript.strip():
#         st.warning("Please paste a transcript.")
#         st.stop()

#     text = transcript.lower()

#     # Sentiment
#     positive = ["thank", "thanks", "good", "great", "happy", "excellent"]
#     negative = ["complaint", "issue", "problem", "angry", "bad", "delay"]

#     sentiment = "Neutral"

#     if any(i in text for i in positive):
#         sentiment = "Positive"

#     if any(i in text for i in negative):
#         sentiment = "Negative"

#     # Summary
#     lines = [i.strip() for i in transcript.split("\n") if i.strip()]

#     summary = f"""
#     Total conversation lines: {len(lines)}

#     Customer contacted regarding {module.lower()} services.
#     Agent responded and handled the discussion.
#     Conversation reviewed successfully.
#     """

#     # Module-specific actions
#     if module == "Loan":
#         actions = [
#             "Verify customer documents",
#             "Check loan eligibility",
#             "Perform credit assessment",
#             "Schedule follow-up"
#         ]

#     elif module == "Insurance":
#         actions = [
#             "Verify policy details",
#             "Check claim status",
#             "Review supporting documents",
#             "Update customer"
#         ]

#     elif module == "Telecom":
#         actions = [
#             "Check network status",
#             "Verify SIM/account",
#             "Create service ticket",
#             "Follow up with customer"
#         ]

#     elif module == "E-Commerce":
#         actions = [
#             "Check order status",
#             "Verify payment",
#             "Process refund/replacement",
#             "Notify customer"
#         ]

#     else:
#         actions = [
#             "Review customer request",
#             "Provide resolution",
#             "Follow up if needed",
#             "Close case"
#         ]

#     risk = "Low"

#     if sentiment == "Negative":
#         risk = "High"

#     st.subheader("📝 Call Summary")
#     st.success(summary)

#     st.subheader("😊 Sentiment")
#     st.info(sentiment)

#     st.subheader("📌 Key Discussion Points")

#     customer_lines = []
#     for line in lines:
#         if line.lower().startswith("customer"):
#             customer_lines.append(line)

#     if customer_lines:
#         for point in customer_lines[:5]:
#             st.write("•", point)
#     else:
#         st.write("• Conversation analyzed.")

#     st.subheader("🎯 Next Best Actions")

#     for action in actions:
#         st.write("✅", action)

#     st.subheader("⚠ Risk Level")

#     if risk == "High":
#         st.error(risk)
#     else:
#         st.success(risk)

#     st.subheader("👨‍💼 Supervisor Recommendation")

#     st.write(
#         f"Review the {module.lower()} interaction and ensure all next-best actions are completed."
#     )
import streamlit as st

st.set_page_config(page_title="AI Call Center Supervisor Assistant", layout="wide")

st.title("📞 AI Call Center Supervisor Assistant")
st.write("Paste any call transcript and get category detection, summary, sentiment, risk, and next-best actions.")

transcript = st.text_area(
    "Paste Call Transcript",
    height=300,
    placeholder="""Customer: I need a home loan.
Agent: Sure sir.
Customer: My salary is ₹75,000.
Customer: I need ₹20 lakh loan.
Agent: We will verify your eligibility."""
)

if st.button("Analyze Transcript"):

    if not transcript.strip():
        st.warning("Please paste a transcript.")
        st.stop()

    text = transcript.lower()

    # -----------------------------
    # Category Detection
    # -----------------------------

    if any(i in text for i in ["loan", "emi", "salary", "credit score", "mortgage"]):
        category = "Loan / Banking"

    elif any(i in text for i in ["insurance", "claim", "policy", "premium"]):
        category = "Insurance"

    elif any(i in text for i in ["network", "sim", "tower", "signal", "recharge"]):
        category = "Telecom"

    elif any(i in text for i in ["order", "refund", "delivery", "product", "shipment"]):
        category = "E-Commerce"

    elif any(i in text for i in ["doctor", "hospital", "appointment", "medicine",
                                 "patient", "health", "treatment", "prescription"]):
        category = "Health"

    elif any(i in text for i in ["credit card", "card limit", "card application"]):
        category = "Credit Card"

    elif any(i in text for i in ["complaint", "issue", "problem", "angry",
                                 "escalate", "unhappy"]):
        category = "Complaint / Support"

    else:
        category = "General"

    # -----------------------------
    # Sentiment Analysis
    # -----------------------------

    positive_words = [
        "thank", "thanks", "good", "great",
        "happy", "excellent", "resolved"
    ]

    negative_words = [
        "angry", "bad", "issue", "problem",
        "complaint", "delay", "unhappy",
        "frustrated", "poor"
    ]

    positive_count = sum(word in text for word in positive_words)
    negative_count = sum(word in text for word in negative_words)

    if positive_count > negative_count:
        sentiment = "Positive"
    elif negative_count > positive_count:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # -----------------------------
    # Risk Level
    # -----------------------------

    if sentiment == "Negative":
        risk = "High"
    elif sentiment == "Neutral":
        risk = "Medium"
    else:
        risk = "Low"

    # -----------------------------
    # Extract Key Customer Lines
    # -----------------------------

    lines = [i.strip() for i in transcript.split("\n") if i.strip()]

    customer_points = []

    for line in lines:
        l = line.lower()

        if l.startswith("customer") or l.startswith("patient"):
            customer_points.append(line)

    # -----------------------------
    # Summary
    # -----------------------------

    summary = f"""
The conversation was identified as **{category}**.

The customer contacted support regarding a matter related to {category.lower()}.
The agent responded and discussed the customer's request.
The interaction was completed and reviewed successfully.

Total conversation lines: {len(lines)}
Customer statements identified: {len(customer_points)}
Sentiment detected: {sentiment}
"""

    # -----------------------------
    # Next Best Actions
    # -----------------------------

    actions = {
        "Loan / Banking": [
            "Verify customer documents",
            "Check loan eligibility",
            "Perform credit assessment",
            "Schedule follow-up call"
        ],
        "Insurance": [
            "Verify policy information",
            "Review claim details",
            "Validate supporting documents",
            "Update customer on status"
        ],
        "Telecom": [
            "Check network/service status",
            "Verify customer account",
            "Create technical ticket",
            "Provide resolution update"
        ],
        "E-Commerce": [
            "Check order details",
            "Verify shipment status",
            "Process refund/replacement if needed",
            "Notify customer"
        ],
        "Health": [
            "Verify patient information",
            "Confirm appointment/treatment details",
            "Share required instructions",
            "Schedule follow-up if needed"
        ],
        "Credit Card": [
            "Verify customer eligibility",
            "Review application details",
            "Perform verification checks",
            "Update application status"
        ],
        "Complaint / Support": [
            "Create support ticket",
            "Escalate issue if required",
            "Assign responsible team",
            "Track resolution"
        ],
        "General": [
            "Review customer request",
            "Provide necessary support",
            "Follow up if needed",
            "Close interaction"
        ]
    }

    # -----------------------------
    # Display Results
    # -----------------------------

    st.subheader("📂 Detected Category")
    st.success(category)

    st.subheader("📝 Call Summary")
    st.write(summary)

    st.subheader("😊 Sentiment")
    st.info(sentiment)

    st.subheader("⚠ Risk Level")

    if risk == "High":
        st.error(risk)
    elif risk == "Medium":
        st.warning(risk)
    else:
        st.success(risk)

    st.subheader("📌 Key Discussion Points")

    if customer_points:
        for point in customer_points[:10]:
            st.write("•", point)
    else:
        st.write("• No specific customer statements identified.")

    st.subheader("🎯 Next Best Actions")

    for action in actions[category]:
        st.write("✅", action)

    st.subheader("👨‍💼 Supervisor Recommendation")

    st.write(
        f"Review the {category.lower()} interaction and ensure all recommended actions are completed."
    )
