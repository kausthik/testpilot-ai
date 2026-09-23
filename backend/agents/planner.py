from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def planner_agent(code: str) -> str:
    prompt = f"""
You are the Planner Agent in TestPilot AI.

Analyze the following code and create a testing plan.

Identify:
1. What the code does
2. Important functions/classes
3. Inputs and outputs
4. Normal test scenarios
5. Edge cases
6. Potential failure points
7. What should be tested for security

Code:

{code}

Return a clear testing plan.
"""

    response = llm.invoke(prompt)

    return response.content