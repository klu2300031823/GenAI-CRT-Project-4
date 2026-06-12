import streamlit as st
import re

st.set_page_config(page_title="Call Center Assistant", layout="wide")

st.title("📞 Call Center Summarization & Next Best Action Assistant")

transcript = st.text_area(
    "Paste Call Transcript",
    height=300
)

def analyze(text):

    lower = text.lower()

    # Sentiment
    pos_words = ["thank", "good", "great", "excellent", "resolved", "happy"]
    neg_words = ["issue", "problem", "delay", "complaint", "refund", "angry",
                 "cancel", "damaged", "disappointed"]

    pos = sum(lower.count(w) for w in pos_words)
    neg = sum(lower.count(w) for w in neg_words)

    if neg > pos:
        sentiment = "Negative 😟"
    elif pos > neg:
        sentiment = "Positive 😊"
    else:
        sentiment = "Neutral 😐"

    # Priority
    high_words = ["angry", "refund", "cancel", "damaged", "urgent"]
    priority = "Low"

    for w in high_words:
        if w in lower:
            priority = "High"
            break

    if "delay" in lower or "issue" in lower:
        priority = "Medium"

    # Customer Issue
    customer_lines = []

    for line in text.split("\n"):
        if line.lower().startswith("customer"):
            customer_lines.append(line)

    issue = customer_lines[0] if customer_lines else "Issue not identified"

    # Summary
    summary = (
        f"The customer contacted support regarding "
        f"{issue.replace('Customer:', '').strip()}. "
        f"The agent interacted with the customer and attempted resolution."
    )

    # Agent score
    score = 100

    if "sorry" in lower or "apologize" in lower:
        score += 10

    if "thank" in lower:
        score += 5

    score = min(score, 100)

    # Next Action
    if "refund" in lower:
        action = "Process refund and update customer."
    elif "loan" in lower:
        action = "Review application and provide status update."
    elif "internet" in lower or "network" in lower:
        action = "Run diagnostics and assign technician."
    elif "insurance" in lower:
        action = "Verify claim and provide update."
    elif "cancel" in lower:
        action = "Forward to retention team."
    else:
        action = "Create support ticket and follow up."

    return {
        "summary": summary,
        "issue": issue,
        "sentiment": sentiment,
        "priority": priority,
        "score": score,
        "action": action
    }

if st.button("Analyze Call"):

    if transcript.strip():

        result = analyze(transcript)

        st.subheader("📋 Executive Summary")
        st.write(result["summary"])

        st.subheader("❗ Customer Issue")
        st.write(result["issue"])

        st.subheader("😊 Sentiment")
        st.write(result["sentiment"])

        st.subheader("⚡ Priority")
        st.write(result["priority"])

        st.subheader("👨‍💼 Agent Performance Score")
        st.progress(result["score"] / 100)
        st.write(f"{result['score']} / 100")

        st.subheader("🎯 Next Best Action")
        st.write(result["action"])

        st.subheader("📝 Supervisor Recommendation")
        st.info(
            "Review the issue, monitor resolution progress, "
            "and ensure customer follow-up is completed."
        )
