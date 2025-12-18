import os
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


def get_agent_response(system_message: str, user_message: str) -> str:
    if not OPENAI_API_KEY or not client:
        return "Error: OpenAI API key not configured. Please add OPENAI_API_KEY to your secrets."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        content = response.choices[0].message.content
        return content if content else "No response generated"
    except Exception as e:
        return f"Error: {str(e)}"


def run_multi_agent_task(user_task: str):
    results = {
        "planner": "",
        "developer": "",
        "reviewer": ""
    }
    
    if not OPENAI_API_KEY:
        error_msg = "Error: OpenAI API key not configured. Please add OPENAI_API_KEY to your secrets."
        return {
            "planner": error_msg,
            "developer": error_msg,
            "reviewer": error_msg,
        }
    
    planner_system = """You are a Planner Agent. Your role is to:
1. Analyze the user's task/goal
2. Break it down into clear, actionable steps
3. Create a structured plan with numbered steps
4. Identify potential challenges and dependencies

Format your response as:
TASK ANALYSIS:
[Brief analysis of the task]

STEP-BY-STEP PLAN:
1. [Step 1]
2. [Step 2]
...

DEPENDENCIES & CONSIDERATIONS:
[List any dependencies or important considerations]

Be concise but thorough."""

    planner_prompt = f"""Please analyze and create a plan for the following task:

USER TASK: {user_task}

Create a detailed step-by-step plan."""

    results["planner"] = get_agent_response(planner_system, planner_prompt)
    
    developer_system = """You are a Developer Agent. Your role is to:
1. Take the plan from the Planner Agent
2. Implement solutions/code for each step
3. Provide working code examples
4. Include comments and explanations

Format your response as:
IMPLEMENTATION:
[For each step in the plan, provide code or detailed solution]

```[language]
[code here]
```

EXPLANATION:
[Brief explanation of the implementation]

USAGE NOTES:
[How to use/run the solution]"""

    developer_prompt = f"""Based on the following plan from the Planner, please implement the solution:

ORIGINAL TASK: {user_task}

PLANNER'S PLAN:
{results["planner"]}

Please implement this plan with working code and detailed explanations."""

    results["developer"] = get_agent_response(developer_system, developer_prompt)
    
    reviewer_system = """You are a Reviewer Agent. Your role is to:
1. Review the Developer's implementation
2. Check for bugs, security issues, and best practices
3. Suggest improvements and optimizations
4. Provide a final polished solution

Format your response as:
REVIEW SUMMARY:
[Overall assessment]

ISSUES FOUND:
- [Issue 1 and fix]
- [Issue 2 and fix]
(or "No critical issues found")

IMPROVEMENTS SUGGESTED:
- [Improvement 1]
- [Improvement 2]

FINAL VERDICT:
[Approved/Needs revision with explanation]"""

    reviewer_prompt = f"""Please review the following implementation:

ORIGINAL TASK: {user_task}

PLANNER'S PLAN:
{results["planner"]}

DEVELOPER'S IMPLEMENTATION:
{results["developer"]}

Please provide a thorough review and any improvements."""

    results["reviewer"] = get_agent_response(reviewer_system, reviewer_prompt)
    
    return results
