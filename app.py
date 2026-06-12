import streamlit as st

st.set_page_config(page_title="Multi-Domain Call Center Supervisor Assistant",
                   layout="wide")

st.title("📞 Multi-Domain Call Center Supervisor Assistant")

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

transcript = st.text_area(
    "Paste Call Transcript",
    height=250
)

def analyze(text, dept):

    text_l = text.lower()

    # Customer issue
    issue = "Not identified"
    for line in text.split("\n"):
        if line.lower().startswith("customer"):
            issue = line.split(":", 1)[1].strip()
            break

    # Sentiment
    positive = ["thank", "good", "great", "happy", "excellent"]
    negative = ["problem", "issue", "delay", "angry",
                "complaint", "cancel", "disappointed"]

    pos = sum(text_l.count(i) for i in positive)
    neg = sum(text_l.count(i) for i in negative)

    if neg > pos:
        sentiment = "Negative 😟"
    elif pos > neg:
        sentiment = "Positive 😊"
    else:
        sentiment = "Neutral 😐"

    # Priority
    priority = "Low"

    if any(x in text_l for x in ["delay", "problem", "issue"]):
        priority = "Medium"

    if any(x in text_l for x in ["angry", "urgent", "emergency"]):
        priority = "High"

    # Agent Score
    score = 50

    if "sorry" in text_l or "apologize" in text_l:
        score += 15

    if "check" in text_l:
        score += 10

    if "review" in text_l:
        score += 10

    if "escalate" in text_l:
        score += 15

    score = min(score, 100)

    # Department Logic

    if dept == "University Admissions":

        intent = "Admission Inquiry"

        action = """
• Share admission guidelines
• Provide application deadlines
• Send eligibility details
"""

        risk = "No Major Risk"

    elif dept == "Loan Services":

        intent = "Loan Inquiry"

        action = """
• Verify loan application
• Check document status
• Update customer
"""

        risk = "Potential Service Delay"

    elif dept == "Survey & Feedback":

        intent = "Feedback Submission"

        action = """
• Record feedback
• Categorize response
• Forward to concerned team
"""

        risk = "No Major Risk"

    elif dept == "Election Information":

        intent = "Election Query"

        action = """
• Provide official election information
• Avoid predictions
• Share election commission resources
"""

        risk = "Misinformation Risk"

    else:

        intent = "Healthcare Inquiry"

        action = """
• Recommend professional consultation
• Provide healthcare resources
• Escalate emergency symptoms
"""

        risk = "Health Advisory Risk"

    summary = (
        f"The customer contacted {dept} regarding '{issue}'. "
        f"The agent handled the inquiry and provided assistance."
    )

    return {
        "summary": summary,
        "issue": issue,
        "intent": intent,
        "sentiment": sentiment,
        "priority": priority,
        "score": score,
        "action": action,
        "risk": risk
    }


if st.button("Analyze Call"):

    if transcript.strip() == "":
        st.warning("Please enter transcript.")

    else:

        result = analyze(transcript, department)

        st.subheader("📋 Executive Summary")
        st.write(result["summary"])

        st.subheader("🏢 Department")
        st.write(department)

        st.subheader("🎯 Customer Intent")
        st.write(result["intent"])

        st.subheader("❗ Customer Issue")
        st.write(result["issue"])

        c1, c2 = st.columns(2)

        with c1:
            st.subheader("😊 Sentiment")
            st.write(result["sentiment"])

        with c2:
            st.subheader("⚡ Priority")
            st.write(result["priority"])

        st.subheader("👨‍💼 Agent Performance Score")
        st.progress(result["score"] / 100)
        st.write(f"{result['score']} / 100")

        st.subheader("🎯 Next Best Actions")
        st.write(result["action"])

        st.subheader("⚠️ Risk Flags")
        st.write(result["risk"])

        st.subheader("📝 Supervisor Recommendation")

        st.info(
            "Review the interaction, verify resolution status, "
            "and ensure appropriate follow-up."
        )

        st.subheader("📊 Dashboard")

        a, b, c = st.columns(3)

        a.metric("Department", department)
        b.metric("Priority", result["priority"])
        c.metric("Agent Score", result["score"])

        feedback = st.radio(
            "Was the analysis useful?",
            ["👍 Yes", "👎 No"]
        )

        if feedback:
            st.success("Feedback Recorded")
