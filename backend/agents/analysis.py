from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def analysis_agent(code: str) -> str:

    prompt = f"""
You are a senior software engineer analyzing source code for automated testing.

Analyze ONLY what is actually present in the code.

IMPORTANT RULES:
- Respect the exact programming language semantics.
- Do not invent validation rules.
- Do not assume parameter types unless the code explicitly enforces them.
- Do not invent exceptions.
- For Python:
  - Integers have arbitrary precision.
  - Normal integer addition does NOT raise OverflowError.
  - Adding floats is valid.
  - Adding strings is valid if both operands are strings.
  - TypeError occurs only for incompatible operand combinations.
  - NaN and infinity are valid float values.
- Clearly distinguish actual behavior from assumptions.

Analyze:

1. Functions/classes
2. Parameters
3. Return values
4. Control flow
5. Dependencies
6. Actual input validation
7. Actual possible exceptions
8. Boundary conditions
9. Important edge cases
10. Potential bugs
11. Security-relevant behavior

For possible exceptions, explain WHY the code can produce them.

CODE:
{code}

Return a concise, technically accurate analysis.
"""

    response = llm.invoke(prompt)

    return response.content