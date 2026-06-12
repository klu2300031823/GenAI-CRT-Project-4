import streamlit as st
import re

st.set_page_config(page_title="Call Center Supervisor Assistant", layout="wide")

st.title("📞 Call Center Summarization & Next-Best-Action Assistant")

transcript = st.text_area(
    "Paste Call Transcript",
    height=300,
    placeholder="""Customer: My loan application is delayed.
Agent: Let me check the status.
Customer: I submitted all documents two weeks ago.
Agent: I will escalate the request."""
)

def analyze(text):

    lower = text.lower()

    # Customer Issue
    issue = "Issue not identified"
    for line in text.split("\n"):
        if line.lower().startswith("customer"):
            issue = line.split(":", 1)[1].strip()
            break

    # Summary
    summary = (
        f"The customer contacted support regarding '{issue}'. "
        f"The agent interacted with the customer and attempted to resolve the concern."
    )

    # Sentiment
    positive = ["thank", "good", "great", "excellent", "happy", "resolved"]
    negative = ["problem", "issue", "delay", "refund", "angry",
                "complaint", "cancel", "damaged", "disappointed"]

    pos = sum(lower.count(w) for w in positive)
    neg = sum(lower.count(w) for w in negative)

    if neg > pos:
        sentiment = "Negative 😟"
    elif pos > neg:
        sentiment = "Positive 😊"
    else:
        sentiment = "Neutral 😐"

    # Priority
    priority = "Low"

    if any(w in lower for w in ["delay", "issue", "problem"]):
        priority = "Medium"

    if any(w in lower for w in ["refund", "cancel", "angry",
                                "fraud", "legal", "damaged"]):
        priority = "High"

    # Agent Score
    score = 50

    if "sorry" in lower or "apologize" in lower:
        score += 10

    if "thank" in lower:
        score += 5

    if "escalate" in lower:
        score += 10

    if "check" in lower or "review" in lower:
        score += 10

    if "resolve" in lower or "resolved" in lower:
        score += 15

    if "don't know" in lower:
        score -= 15

    if "cannot help" in lower:
        score -= 20

    if "call again" in lower:
        score -= 10

    score = max(0, min(score, 100))

    # Next Best Actions
    actions = []

    if "refund" in lower:
        actions.append("Verify refund eligibility.")
        actions.append("Process refund request.")

    if "damaged" in lower:
        actions.append("Arrange replacement or return process.")

    if "loan" in lower:
        actions.append("Review loan processing status.")
        actions.append("Update customer on pending verification.")

    if "insurance" in lower:
        actions.append("Check claim status.")
        actions.append("Verify supporting documents.")

    if "internet" in lower or "network" in lower:
        actions.append("Run technical diagnostics.")
        actions.append("Schedule technician visit.")

    if "cancel" in lower:
        actions.append("Forward case to retention team.")
        actions.append("Offer retention benefits.")

    if "payment" in lower or "transaction" in lower:
        actions.append("Investigate transaction details.")
        actions.append("Provide refund/reversal timeline.")

    if not actions:
        actions.append("Create support ticket.")
        actions.append("Schedule customer follow-up.")

    # Risk Flags
    risks = []

    if "angry" in lower:
        risks.append("High Customer Dissatisfaction")

    if "refund" in lower:
        risks.append("Refund Escalation Risk")

    if "cancel" in lower:
        risks.append("Customer Churn Risk")

    if "fraud" in lower:
        risks.append("Fraud Investigation Required")

    if "legal" in lower:
        risks.append("Legal Escalation Risk")

    if not risks:
        risks.append("No Major Risks Detected")

    # Compliance Check
    compliance = "✓ No policy violations detected"

    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\d{10}"

    if re.search(email_pattern, text) or re.search(phone_pattern, text):
        compliance = "⚠️ Sensitive Information Detected"

    return {
        "summary": summary,
        "issue": issue,
        "sentiment": sentiment,
        "priority": priority,
        "score": score,
        "actions": actions,
        "risks": risks,
        "compliance": compliance
    }


if st.button("Analyze Call"):

    if transcript.strip() == "":
        st.warning("Please enter a transcript.")

    else:

        result = analyze(transcript)

        st.subheader("📋 Executive Summary")
        st.write(result["summary"])

        st.subheader("❗ Customer Issue")
        st.write(result["issue"])

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("😊 Sentiment")
            st.write(result["sentiment"])

        with col2:
            st.subheader("⚡ Priority")
            st.write(result["priority"])

        st.subheader("👨‍💼 Agent Performance Score")
        st.progress(result["score"] / 100)
        st.write(f"{result['score']} / 100")

        st.subheader("🎯 Next Best Actions")
        for i, action in enumerate(result["actions"], start=1):
            st.write(f"{i}. {action}")

        st.subheader("⚠️ Risk Flags")
        for risk in result["risks"]:
            st.write("•", risk)

        st.subheader("🛡️ Compliance Check")
        st.write(result["compliance"])

        st.subheader("📊 Supervisor Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Calls Analyzed", "1")
        c2.metric("Priority", result["priority"])
        c3.metric("Agent Score", result["score"])
        c4.metric("Risk Flags", len(result["risks"]))

        st.subheader("📝 Supervisor Recommendation")

        st.info(
            "Review the issue, monitor resolution progress, "
            "verify customer satisfaction, and ensure follow-up actions are completed."
        )

        st.subheader("🔄 Feedback")

        feedback = st.radio(
            "Was this analysis useful?",
            ["👍 Yes", "👎 No"]
        )

        if feedback:
            st.success("Feedback recorded.")
