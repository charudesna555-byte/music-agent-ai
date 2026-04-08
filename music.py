import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ReviewFlow",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --bg: #f3f1ec;
        --surface: #fbfaf7;
        --surface-2: #f6f3ee;
        --panel: #ffffff;
        --line: #ddd8cf;
        --text: #2e2b27;
        --muted: #6f6a63;
        --green: #6f8f72;
        --green-soft: #e5ede5;
        --blue: #7b92a8;
        --blue-soft: #e7edf3;
        --amber: #b7925b;
        --amber-soft: #f3eadb;
        --red: #b86c63;
        --red-soft: #f4e3e0;
        --radius-lg: 18px;
        --radius-md: 14px;
        --radius-sm: 10px;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
    }

    .block-container {
        max-width: 1350px;
        padding-top: 1.25rem;
        padding-bottom: 1.5rem;
    }

    section[data-testid="stSidebar"] {
        display: none;
    }

    .topbar {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
    }

    .app-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: var(--text);
        margin-bottom: 0.25rem;
    }

    .app-subtitle {
        font-size: 0.95rem;
        color: var(--muted);
        line-height: 1.6;
    }

    .pill {
        display: inline-block;
        padding: 0.42rem 0.8rem;
        border-radius: 999px;
        background: var(--surface-2);
        border: 1px solid var(--line);
        color: var(--muted);
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.2rem 0.25rem 0 0;
    }

    .panel {
        background: var(--panel);
        border: 1px solid var(--line);
        border-radius: var(--radius-lg);
        padding: 1.1rem;
        margin-bottom: 1rem;
    }

    .soft-panel {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: var(--radius-lg);
        padding: 1rem;
        margin-bottom: 1rem;
    }

    .section-title {
        font-size: 1rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 0.7rem;
    }

    .section-copy {
        font-size: 0.92rem;
        color: var(--muted);
        line-height: 1.6;
    }

    .stat-card {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 16px;
        padding: 1rem;
        min-height: 108px;
    }

    .stat-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--muted);
        font-weight: 700;
        margin-bottom: 0.38rem;
    }

    .stat-value {
        font-size: 1.1rem;
        font-weight: 800;
        color: var(--text);
        margin-bottom: 0.28rem;
    }

    .stat-desc {
        font-size: 0.84rem;
        line-height: 1.45;
        color: var(--muted);
    }

    .status-box {
        border-radius: 14px;
        padding: 0.9rem 1rem;
        text-align: center;
        font-size: 0.95rem;
        font-weight: 700;
        margin-bottom: 1rem;
        border: 1px solid var(--line);
    }

    .excellent {
        background: var(--green-soft);
        color: #4e6751;
    }

    .good {
        background: var(--blue-soft);
        color: #52687d;
    }

    .warning {
        background: var(--amber-soft);
        color: #81673c;
    }

    .risk {
        background: var(--red-soft);
        color: #8d554e;
    }

    .data-box {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 0.95rem;
    }

    .data-row {
        display: flex;
        justify-content: space-between;
        gap: 0.8rem;
        padding: 0.58rem 0;
        border-bottom: 1px solid #ece7df;
    }

    .data-row:last-child {
        border-bottom: none;
    }

    .data-key {
        font-size: 0.9rem;
        color: var(--muted);
        font-weight: 600;
    }

    .data-value {
        font-size: 0.9rem;
        color: var(--text);
        font-weight: 700;
        text-align: right;
    }

    .tag {
        display: inline-block;
        padding: 0.42rem 0.75rem;
        border-radius: 999px;
        border: 1px solid var(--line);
        background: var(--surface-2);
        color: var(--text);
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.18rem;
    }

    .summary-box {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 0.95rem 1rem;
        color: var(--text);
        font-size: 0.92rem;
        line-height: 1.65;
    }

    .side-note {
        background: var(--surface-2);
        border: 1px solid var(--line);
        border-radius: 14px;
        padding: 0.95rem;
        color: var(--muted);
        font-size: 0.88rem;
        line-height: 1.55;
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div,
    .stTextInput > div > div,
    .stSelectbox > div > div {
        background: #ffffff !important;
        border: 1px solid var(--line) !important;
        border-radius: 12px !important;
        min-height: 46px;
        box-shadow: none !important;
    }

    input, textarea, [data-baseweb="input"] input {
        color: var(--text) !important;
        -webkit-text-fill-color: var(--text) !important;
        caret-color: var(--text) !important;
        font-size: 15px !important;
    }

    input::placeholder, textarea::placeholder {
        color: #9a948a !important;
        -webkit-text-fill-color: #9a948a !important;
    }

    .stTextInput label, .stSelectbox label {
        color: var(--text) !important;
        font-weight: 600 !important;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 0.82rem 1rem;
        font-size: 0.95rem;
        font-weight: 700;
        border: 1px solid #6f8f72;
        background: #6f8f72;
        color: white;
        box-shadow: none;
    }

    .stProgress > div > div > div > div {
        background: #6f8f72 !important;
    }

    .stProgress > div > div {
        background-color: #e7e2d8 !important;
    }

    .footer {
        text-align: center;
        color: var(--muted);
        font-size: 0.82rem;
        padding-top: 0.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

def evaluate_review(goal_score, manager_score, peer_score, self_score, completion, bias_signal):
    weighted_score = (
        goal_score * 0.35 +
        manager_score * 0.30 +
        peer_score * 0.20 +
        self_score * 0.15
    )
    weighted_score = round(weighted_score, 2)

    variance = max(goal_score, manager_score, peer_score, self_score) - min(goal_score, manager_score, peer_score, self_score)

    fairness = 95
    if variance >= 3:
        fairness -= 20
    elif variance >= 2:
        fairness -= 12
    elif variance >= 1:
        fairness -= 6

    if completion < 60:
        fairness -= 14
    elif completion < 80:
        fairness -= 6

    if bias_signal == "Medium":
        fairness -= 10
    elif bias_signal == "High":
        fairness -= 20

    fairness = max(40, min(98, fairness))

    if weighted_score >= 4.3 and fairness >= 80:
        label = "Exceeds Expectations"
        status = "excellent"
    elif weighted_score >= 3.5:
        label = "Meets Expectations"
        status = "good"
    elif weighted_score >= 2.8:
        label = "Needs Development Support"
        status = "warning"
    else:
        label = "Review Attention Required"
        status = "risk"

    return weighted_score, fairness, variance, label, status

def generate_development_plan(label):
    if label == "Exceeds Expectations":
        return [
            "Lead one cross-functional initiative",
            "Mentor a junior teammate",
            "Prepare a promotion-readiness plan"
        ]
    elif label == "Meets Expectations":
        return [
            "Improve one core skill with monthly checkpoints",
            "Own a measurable deliverable",
            "Strengthen stakeholder communication"
        ]
    elif label == "Needs Development Support":
        return [
            "Set 30-day improvement goals",
            "Schedule weekly manager coaching",
            "Track blockers and progress regularly"
        ]
    else:
        return [
            "Begin a structured improvement plan",
            "Clarify performance expectations",
            "Review progress every week"
        ]

load_css()

st.markdown("""
<div class="topbar">
    <div class="app-title">ReviewFlow</div>
    <div class="app-subtitle">
        Automated performance review system for fair, structured, and consistent employee evaluations.
    </div>
    <div style="margin-top:0.65rem;">
        <span class="pill">Standardized Criteria</span>
        <span class="pill">360 Feedback</span>
        <span class="pill">Bias Mitigation</span>
        <span class="pill">Development Planning</span>
    </div>
</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4, gap="large")
with s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Review Coverage</div>
        <div class="stat-value">91%</div>
        <div class="stat-desc">Most active reviews include structured manager and peer input.</div>
    </div>
    """, unsafe_allow_html=True)
with s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Consistency</div>
        <div class="stat-value">Stable</div>
        <div class="stat-desc">Shared criteria improve comparability across evaluations.</div>
    </div>
    """, unsafe_allow_html=True)
with s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Bias Alerts</div>
        <div class="stat-value">Low</div>
        <div class="stat-desc">Review gaps and rating outliers can be flagged for validation.</div>
    </div>
    """, unsafe_allow_html=True)
with s4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-label">Goal Progress</div>
        <div class="stat-value">79%</div>
        <div class="stat-desc">Average progress across current employee review cycles.</div>
    </div>
    """, unsafe_allow_html=True)

left, right = st.columns([1.15, 1], gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Create Review</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-copy">Enter structured performance inputs to generate a fair review summary, confidence score, and development plan.</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with st.form("review_form"):
        c1, c2 = st.columns(2, gap="large")
        with c1:
            employee = st.text_input("Employee Name", "Nisha Raman")
            role = st.selectbox("Role", ["Software Engineer", "Product Designer", "HR Analyst", "Project Coordinator"])
            department = st.selectbox("Department", ["Engineering", "Design", "HR", "Operations"])
            review_period = st.selectbox("Review Period", ["Q1 2026", "Q2 2026", "Annual 2026"])
            goal_score = st.selectbox("Goal Achievement Score", [1, 2, 3, 4, 5], index=3)
        with c2:
            manager_score = st.selectbox("Manager Review Score", [1, 2, 3, 4, 5], index=3)
            peer_score = st.selectbox("Peer Feedback Score", [1, 2, 3, 4, 5], index=3)
            self_score = st.selectbox("Self Assessment Score", [1, 2, 3, 4, 5], index=3)
            completion = st.slider("Goal Completion %", 0, 100, 78)
            bias_signal = st.selectbox("Bias Risk Signal", ["Low", "Medium", "High"])

        strengths = st.text_input("Key Strengths", "Collaboration, delivery quality, accountability")
        development_need = st.text_input("Development Need", "Decision-making speed during deadline pressure")
        submitted = st.form_submit_button("Generate Review")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="soft-panel">
        <div class="section-title">Evaluation Framework</div>
        <span class="tag">Role-aligned scoring</span>
        <span class="tag">Multi-source feedback</span>
        <span class="tag">Bias checks</span>
        <span class="tag">Development goals</span>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Review Output</div>', unsafe_allow_html=True)

    if submitted:
        weighted_score, fairness, variance, label, status = evaluate_review(
            goal_score, manager_score, peer_score, self_score, completion, bias_signal
        )
        dev_plan = generate_development_plan(label)
        generated_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.markdown(f'<div class="status-box {status}">{label} — Fairness confidence {fairness}/100</div>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="data-box">
            <div class="data-row"><div class="data-key">Employee</div><div class="data-value">{employee}</div></div>
            <div class="data-row"><div class="data-key">Role</div><div class="data-value">{role}</div></div>
            <div class="data-row"><div class="data-key">Department</div><div class="data-value">{department}</div></div>
            <div class="data-row"><div class="data-key">Review Period</div><div class="data-value">{review_period}</div></div>
            <div class="data-row"><div class="data-key">Generated At</div><div class="data-value">{generated_time}</div></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        m1, m2 = st.columns(2, gap="medium")
        with m1:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Composite Score</div>
                <div class="stat-value">{weighted_score}/5</div>
                <div class="stat-desc">Weighted from goals, manager, peer, and self inputs.</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-label">Score Variance</div>
                <div class="stat-value">{variance}</div>
                <div class="stat-desc">Useful for consistency checks and calibration review.</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        summary = (
            f"{employee} is rated as '{label}' for the {role} role based on weighted goal achievement, "
            f"manager review, peer feedback, and self-assessment. The system generated a composite score of "
            f"{weighted_score}/5 with a fairness confidence of {fairness}/100. Key strengths include "
            f"{strengths.lower()}, while the main development focus is {development_need.lower()}."
        )

        st.markdown('<div class="section-title">Generated Summary</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="section-title">Development Plan</div>', unsafe_allow_html=True)
        st.markdown("".join([f'<span class="tag">{item}</span>' for item in dev_plan]), unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">Confidence</div>', unsafe_allow_html=True)
        st.progress(fairness)

    else:
        st.markdown("""
        <div class="side-note">
            Fill in the review form to generate a simple, structured, and bias-aware performance review with a development plan.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="stat-card">
            <div class="stat-label">Why this UI</div>
            <div class="stat-value">Simple and readable</div>
            <div class="stat-desc">Flat cards, matte colors, and minimal styling keep the review workflow clear and professional.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Performance review system with simple matte flat UI for fair and consistent evaluations.</div>', unsafe_allow_html=True)
