from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def test_generator_agent(code: str, analysis: str) -> str:

    prompt = f"""
You are a senior Python software test engineer.

Generate test cases for the EXACT code provided.

CRITICAL:
The CODE is the source of truth.
The ANALYSIS is supporting information and may contain mistakes.

Before generating each test, verify that the expected behavior is
actually possible according to the code and Python semantics.

NEVER invent:
- validation rules
- exceptions
- type restrictions
- overflow errors
- unsupported behavior

Python rules:
- Python integers have arbitrary precision.
- Integer addition does not normally raise OverflowError.
- Floating-point values are valid unless explicitly rejected.
- NaN and infinity are valid float values.
- Strings can be added to strings.
- Incompatible operands can raise TypeError.

For every test provide:

- Test name
- Input
- Expected output
- Expected exception, ONLY if actually possible
- Reason

Include:

1. Happy path
2. Edge cases
3. Boundary cases
4. Valid unusual inputs
5. Invalid inputs
6. Exception cases
7. Regression cases

If a category is not applicable, say:
"Not applicable."

CODE:
{code}

ANALYSIS:
{analysis}

Return only accurate and code-specific test cases.
"""

    response = llm.invoke(prompt)

    return response.content