import streamlit as st
from agents import run_multi_agent_task

st.set_page_config(
    page_title="AI Multi-Agent Task Manager",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.agent-card {
    background-color: #f0f2f6;
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0;
    border-left: 5px solid;
}
.planner-card {
    border-left-color: #1f77b4;
}
.developer-card {
    border-left-color: #2ca02c;
}
.reviewer-card {
    border-left-color: #ff7f0e;
}
.agent-title {
    font-size: 1.3em;
    font-weight: bold;
    margin-bottom: 10px;
}
.stButton>button {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Multi-Agent Task Manager")
st.markdown("""
Welcome to the **AI Multi-Agent Task Manager**! This application uses three specialized AI agents 
that work together to help you accomplish complex tasks:

- **🎯 Planner Agent**: Analyzes your task and creates a structured plan
- **💻 Developer Agent**: Implements solutions based on the plan  
- **🔍 Reviewer Agent**: Reviews and improves the implementation

Enter your task below and watch the agents collaborate!
""")

st.divider()

user_task = st.text_area(
    "📝 Enter your task or goal:",
    placeholder="Example: Build a login system with email and password authentication",
    height=100
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_button = st.button("🚀 Run Agents", use_container_width=True)

if run_button:
    if not user_task.strip():
        st.error("⚠️ Please enter a task before running the agents.")
    else:
        st.divider()
        st.subheader("🔄 Agent Responses")
        
        with st.spinner("🤖 Agents are working on your task... This may take a moment."):
            results = run_multi_agent_task(user_task)
        
        st.success("✅ All agents have completed their work!")
        
        st.markdown("### 🎯 Planner Agent")
        with st.container():
            st.markdown(f"""
            <div class="agent-card planner-card">
                <div class="agent-title">📋 Task Planning</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(results["planner"])
        
        st.markdown("### 💻 Developer Agent")
        with st.container():
            st.markdown(f"""
            <div class="agent-card developer-card">
                <div class="agent-title">🛠️ Implementation</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(results["developer"])
        
        st.markdown("### 🔍 Reviewer Agent")
        with st.container():
            st.markdown(f"""
            <div class="agent-card reviewer-card">
                <div class="agent-title">✅ Review & Improvements</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(results["reviewer"])

st.divider()
st.markdown("""
---
<div style="text-align: center; color: #666;">
    <p>Built with Streamlit and AutoGen | Powered by OpenAI</p>
</div>
""", unsafe_allow_html=True)
