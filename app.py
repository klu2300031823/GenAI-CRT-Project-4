import streamlit as st
import re

st.set_page_config(page_title="Call Center Supervisor Assistant", layout="wide")

st.title("📞 Call-Center Summarization & Next-Best-Action Assistant")

st.write("Paste a customer-agent conversation and get a summary, sentiment, key issues, and next-best actions.")

# ---------- FUNCTIONS ----------

def summarize_call(text):
    lines = [i.strip() for i in text.split("\n") if i.strip()]

    customer_lines = []
    agent_lines = []

    for line in lines:
        if line.lower().startswith("customer"):
            customer_lines.append(line)
        elif line.lower().startswith("agent"):
            agent_lines.append(line)

    summary = []

    if customer_lines:
        summary.append("Customer contacted support regarding an issue.")

    if agent_lines:
        summary.append("Agent responded and provided assistance.")

    return " ".join(summary)


def detect_sentiment(text):
    text = text.lower()

    positive = ["thank", "good", "great", "happy", "resolved", "excellent"]
    negative = ["problem", "issue", "bad", "angry", "cancel", "refund", "complaint"]

    pos = sum(text.count(word) for word in positive)
    neg = sum(text.count(word) for word in negative)

    if neg > pos:
        return "Negative 😟"
    elif pos > neg:
        return "Positive 😊"
    else:
        return "Neutral 😐"


def find_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())

    ignore = {
        "customer","agent","hello","please","thank",
        "thanks","there","their","about","would",
        "could","have","your","with","this"
    }

    freq = {}

    for word in words:
        if word not in ignore:
            freq[word] = freq.get(word, 0) + 1

    keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return [k[0] for k in keywords[:5]]


def next_best_action(text):
    t = text.lower()

    if "refund" in t:
        return [
            "Verify refund eligibility",
            "Escalate to billing team",
            "Follow up within 24 hours"
        ]

    if "cancel" in t:
        return [
            "Offer retention discount",
            "Explain available plans",
            "Escalate if customer still wants cancellation"
        ]

    if "loan" in t:
        return [
            "Verify customer documents",
            "Check loan eligibility",
            "Schedule callback"
        ]

    if "insurance" in t:
        return [
            "Verify policy details",
            "Provide claim information",
            "Create service ticket"
        ]

    return [
        "Create support ticket",
        "Monitor customer satisfaction",
        "Schedule follow-up call"
    ]


# ---------- UI ----------

conversation = st.text_area(
    "Paste Call Transcript",
    height=350,
    placeholder="""Customer: My loan application is delayed.
Agent: Let me check the status.
Customer: I submitted all documents last week.
Agent: We will escalate the request."""
)

if st.button("Analyze Call"):

    if conversation.strip() == "":
        st.warning("Please enter a transcript.")
    else:

        summary = summarize_call(conversation)
        sentiment = detect_sentiment(conversation)
        keywords = find_keywords(conversation)
        actions = next_best_action(conversation)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📋 Call Summary")
            st.write(summary)

            st.subheader("😊 Sentiment")
            st.success(sentiment)

        with col2:
            st.subheader("🔑 Key Topics")
            for k in keywords:
                st.write("•", k)

        st.subheader("🎯 Next Best Actions")

        for i, action in enumerate(actions, start=1):
            st.write(f"{i}. {action}")

        st.subheader("👨‍💼 Supervisor Notes")

        st.info(
            "Review customer concern, verify resolution status, "
            "and ensure follow-up actions are completed."
        )
