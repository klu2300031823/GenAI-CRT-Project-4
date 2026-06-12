import streamlit as st

st.set_page_config(page_title="AI Supervisor Assistant", layout="wide")
st.title("📞 Smart Call-Center Assistant")

# -----------------------------
# MODULE QUESTIONS
# -----------------------------
questions = {
    "University Admission": [
        ("What is the user's need?", ["New admission", "Transfer", "Scholarship inquiry"]),
        ("What level?", ["Undergraduate", "Postgraduate", "PhD"]),
        ("Urgency?", ["Immediate", "Within 1 month", "Just exploring"])
    ],

    "Loan": [
        ("Loan type?", ["Home loan", "Personal loan", "Education loan"]),
        ("User status?", ["Salaried", "Self-employed", "Student"]),
        ("Urgency?", ["Urgent", "Normal", "Just enquiry"])
    ],

    "Survey": [
        ("Customer sentiment?", ["Positive", "Neutral", "Negative"]),
        ("Main issue?", ["Service delay", "Pricing", "Support quality"]),
        ("Feedback type?", ["Complaint", "Suggestion", "Appreciation"])
    ],

    "Election": [
        ("Region?", ["State", "National"]),
        ("Voter trend?", ["Pro-current govt", "Opposition", "Undecided"]),
        ("Source?", ["Survey data", "Social media", "News"])
    ],

    "Healthcare": [
        ("Symptom type?", ["Fever", "Pain", "Chronic issue"]),
        ("Severity?", ["Mild", "Moderate", "Severe"]),
        ("Duration?", ["1-2 days", "1 week", "More than 1 week"])
    ]
}

# -----------------------------
# SESSION STATE
# -----------------------------
if "answers" not in st.session_state:
    st.session_state.answers = {}

if "step" not in st.session_state:
    st.session_state.step = 0


# -----------------------------
# MODULE SELECTION
# -----------------------------
module = st.selectbox("Select Module", list(questions.keys()))

selected_questions = questions[module]

st.markdown("---")

# -----------------------------
# STEP-BY-STEP QUESTION FLOW
# -----------------------------
if st.session_state.step < len(selected_questions):

    q, options = selected_questions[st.session_state.step]

    st.subheader(f"Q{st.session_state.step+1}: {q}")

    answer = st.radio("Choose an option", options)
    custom = st.text_input("Or type your own response")

    if st.button("Next"):

        final_answer = custom if custom else answer
        st.session_state.answers[q] = final_answer
        st.session_state.step += 1
        st.rerun()

# -----------------------------
# FINAL OUTPUT
# -----------------------------
else:

    st.subheader("📌 Interaction Summary")

    summary = f"This call is related to {module}. Key details:\n"
    for q, a in st.session_state.answers.items():
        summary += f"- {q}: {a}\n"

    st.write(summary)

    # -----------------------------
    # NEXT BEST ACTION LOGIC
    # -----------------------------
    st.subheader("✅ Next Best Action")

    if module == "University Admission":
        action = "Provide admission process, eligibility, and deadlines."

    elif module == "Loan":
        action = "Check eligibility and suggest required documents."

    elif module == "Survey":
        action = "Identify issues and escalate if negative feedback."

    elif module == "Election":
        action = "Summarize trends cautiously; avoid definitive predictions."

    elif module == "Healthcare":
        action = "Provide general guidance and suggest consulting a doctor."

    st.success(action)

    # -----------------------------
    # RESET OPTION
    # -----------------------------
    if st.button("Start New Interaction"):
        st.session_state.answers = {}
        st.session_state.step = 0
        st.rerun()
