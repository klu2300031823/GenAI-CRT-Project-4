import streamlit as st
from datetime import datetime
import random

# -----------------------------
# SIMULATED LLM RESPONSE
# (Replace with OpenAI / Azure / local model later)
# -----------------------------
def generate_response(module, user_input):
    summary = f"This interaction is related to {module}. The user is asking about: {user_input}."

    next_actions = {
        "University Admission": [
            "Provide eligibility criteria and required documents",
            "Guide through application portal",
            "Suggest deadlines and scholarship options"
        ],
        "Loan": [
            "Check loan eligibility",
            "Suggest documents required",
            "Recommend suitable loan schemes"
        ],
        "Survey": [
            "Analyze customer sentiment",
            "Identify improvement areas",
            "Recommend corrective actions"
        ],
        "Election": [
            "Summarize recent trends",
            "Highlight leading candidates",
            "Suggest caution: Predictions may change"
        ],
        "Healthcare": [
            "Provide general information on symptoms",
            "Recommend consulting doctor",
            "Suggest preventive measures"
        ]
    }

    action = random.choice(next_actions[module])

    return summary, action


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Supervisor AI Assistant", layout="wide")

st.title("📞 Call-Center Supervisor Assistant")
st.markdown("Summarization + Next Best Action Recommendation")

# -----------------------------
# MODULE SELECTION
# -----------------------------
module = st.selectbox(
    "Select Domain Module",
    ["University Admission", "Loan", "Survey", "Election", "Healthcare"]
)

# -----------------------------
# USER INPUT
# -----------------------------
user_input = st.text_area("Enter Customer Interaction Text")

if st.button("Analyze Interaction"):

    if not user_input.strip():
        st.warning("⚠ Please enter some interaction text")
    else:
        with st.spinner("Processing..."):

            summary, next_action = generate_response(module, user_input)

            # Output Section
            st.subheader("📌 Interaction Summary")
            st.write(summary)

            st.subheader("✅ Next Best Action")
            st.success(next_action)

            # Metrics (Mock for pilot)
            st.subheader("📊 System Metrics")
            st.write({
                "Latency (ms)": random.randint(200, 800),
                "Confidence Score": round(random.uniform(0.7, 0.95), 2),
                "Hallucination Risk": "Low",
                "GPU Cost per 100 requests": "$0.45 (simulated)"
            })

# -----------------------------
# FEEDBACK LOOP
# -----------------------------
st.markdown("---")
st.subheader("📝 Supervisor Feedback")

feedback = st.radio("Was the response useful?", ["Yes", "No"])

if st.button("Submit Feedback"):
    st.success("✅ Feedback recorded (simulated logging)")
