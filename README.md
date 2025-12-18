AI Multi-Agent Task Manager

A full-stack AI application that uses multiple specialized AI agents to help you accomplish complex tasks. Built with Python, AutoGen, and Streamlit.

What This Project Does

This application leverages the power of AI multi-agent systems to break down, implement, and refine solutions for any task you provide. Three specialized agents work together autonomously:

Planner Agent: Analyzes your task and creates a detailed, step-by-step plan
Developer Agent: Implements the plan with working code and explanations
Reviewer Agent: Reviews the implementation and suggests improvements
Tech Stack

Python 3.11 - Core programming language
AutoGen - Microsoft's framework for building multi-agent AI systems
Streamlit - Modern web framework for the user interface
OpenAI GPT - Language model powering the agents
How the AI Agents Work

Agent Communication Flow

User Task → Planner Agent → Developer Agent → Reviewer Agent → Final Output

User Input: You provide a task or goal (e.g., "Build a login system")
Planner Agent:
Analyzes the task requirements
Breaks it into actionable steps
Identifies dependencies and considerations
Developer Agent:
Receives the plan from Planner
Implements solutions with code
Provides explanations and usage notes
Reviewer Agent:
Reviews the Developer's implementation
Checks for bugs and security issues
Suggests optimizations and best practices
Provides a final polished solution
Autonomous Collaboration

The agents communicate by passing their outputs as context to the next agent, creating a seamless pipeline that mimics a real development team workflow.

Project Structure

├── app.py              # Streamlit frontend application
├── agents.py           # AutoGen agents logic and configuration
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .streamlit/
    └── config.toml     # Streamlit server configuration

How to Run on Replit

Prerequisites

Fork or clone this project on Replit
Add your OpenAI API key to Replit Secrets:
Click on "Secrets" in the Tools panel
Add a new secret with key OPENAI_API_KEY
Paste your OpenAI API key as the value
Running the Application

The application will automatically start when you click "Run"
The Streamlit server will launch on port 5000
Enter your task in the text area
Click "Run Agents" to start the multi-agent collaboration
View responses from each agent in separate sections
Usage Examples

Here are some tasks you can try:

"Build a login system with email and password authentication"
"Create a machine learning pipeline for sentiment analysis"
"Design a REST API for a todo application"
"Build a web scraper for news articles"
"Create a database schema for an e-commerce platform"
Configuration

The agents use GPT-4o-mini by default for cost efficiency. You can modify the model in agents.py:

llm_config = {
    "config_list": [
        {
            "model": "gpt-4o-mini",  # Change to "gpt-4" for more powerful responses
            "api_key": OPENAI_API_KEY,
        }
    ],
}

Features

Clean, modern Streamlit UI
Real-time loading spinner while agents work
Separate display sections for each agent's response
Color-coded agent cards for easy identification
Responsive design that works on all devices
Error handling for missing API keys
License

MIT License - Feel free to use and modify for your own projects.

Acknowledgments

Microsoft AutoGen - Multi-agent framework
Streamlit - Web application framework
OpenAI - Language model provider
