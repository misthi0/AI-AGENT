AI Multi-Agent Task Manager

Overview

This is a full-stack AI application that uses Microsoft's AutoGen framework to orchestrate multiple specialized AI agents for task completion. The system implements a pipeline workflow where three agents (Planner, Developer, Reviewer) collaborate autonomously to analyze, implement, and refine solutions for user-provided tasks. The frontend is built with Streamlit, providing a web-based interface for users to interact with the multi-agent system.

User Preferences

Preferred communication style: Simple, everyday language.

System Architecture

Multi-Agent Pipeline Design

The application follows a sequential agent communication pattern where each agent's output becomes the context for the next agent. This mimics a real development team workflow.

Agent Roles:

Planner Agent: First in pipeline - analyzes tasks and creates structured, step-by-step plans
Developer Agent: Second in pipeline - implements solutions with working code based on the plan
Reviewer Agent: Final in pipeline - reviews implementation, identifies issues, and suggests improvements
Design Decision: Sequential pipeline over parallel execution was chosen to ensure each agent builds upon the previous agent's work, creating coherent and refined outputs.

Frontend Architecture

Streamlit: Chosen for rapid prototyping and simple deployment of data/AI applications
Single-page application with custom CSS styling for agent-specific card components
Wide layout configuration for better content display
Backend Architecture

Pure Python: No separate backend server - Streamlit handles both UI and business logic
agents.py: Contains agent factory functions and model client configuration
app.py: Streamlit application entry point with UI components
main.py: Currently empty, potentially reserved for CLI or alternative entry points
AI Model Integration

AutoGen Framework: Microsoft's multi-agent orchestration framework handles agent communication and message passing
OpenAI GPT-4o-mini: Language model powering all agents, accessed via OpenAI API
Model client is instantiated per-agent using a factory function pattern
Configuration Pattern

Environment variables for sensitive data (OPENAI_API_KEY)
Hardcoded model selection (gpt-4o-mini) - could be made configurable
System prompts defined inline within agent creation functions
External Dependencies

AI/ML Services

OpenAI API: Provides GPT-4o-mini model access for agent intelligence. Requires OPENAI_API_KEY environment variable.
Python Packages

autogen-agentchat (>=0.7.5): Core multi-agent framework for creating and orchestrating AI agents
autogen-ext (>=0.7.5): AutoGen extensions including OpenAI model client integration
openai (>=1.0.0): Official OpenAI Python client library
streamlit (>=1.28.0): Web application framework for the user interface
tiktoken (>=0.5.0): OpenAI's tokenizer for token counting and management
Environment Requirements

Python 3.11
OPENAI_API_KEY must be set in environment variables for the application to function
