from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def security_agent(code: str) -> str:
    prompt = f"""
You are the Security Agent in TestPilot AI.

Review the following code for potential security vulnerabilities.

Look for:
- Injection vulnerabilities
- Authentication/authorization issues
- Sensitive data exposure
- Unsafe input handling
- Insecure dependencies
- Hardcoded secrets
- Improper error handling
- Other security risks

For each finding provide:
- Severity
- Vulnerability
- Explanation
- Suggested mitigation

Code:

{code}
"""

    response = llm.invoke(prompt)

    return response.content