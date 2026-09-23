from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def testpilot_agent(code: str) -> str:

    prompt = f"""
You are TestPilot AI, an expert Python testing assistant.

Analyze ONLY the provided code.

Return ONLY valid JSON. No markdown. No explanation outside JSON.

Format:

{{
  "analysis": "brief description",
  "test_cases": [
    {{
      "name": "test name",
      "input": "example input",
      "expected": "expected output or exception",
      "reason": "why this test matters"
    }}
  ],
  "security": "security findings or None"
}}

Rules:
- Do not invent behavior.
- Do not mention irrelevant operations.
- Do not mention division by zero unless the code performs division.
- Python integers do not normally overflow.
- Floats are valid unless explicitly rejected.
- Strings can be added to strings.
- Only report TypeError when the actual operation causes it.
- Keep it concise.
- Generate 5-8 useful tests.

CODE:
{code}
"""

    response = llm.invoke(prompt)

    return response.content