from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)


def reviewer_agent(
    code: str,
    analysis: str,
    test_cases: str,
    security_report: str
) -> str:

    prompt = f"""
You are the final quality reviewer for an AI software testing system.

Your MOST IMPORTANT responsibility is detecting hallucinated or
technically incorrect tests.

The CODE is the source of truth.

Review every generated test.

For each problematic test identify:
- Test
- VALID or INVALID
- Reason
- Corrected test if INVALID

Check specifically for:
- Impossible exceptions
- Incorrect expected outputs
- Invented validation rules
- Incorrect language semantics
- Missing important edge cases
- Tests unrelated to the code
- Incorrect security findings

Python reminders:
- Integer arithmetic has arbitrary precision.
- Normal integer addition does not raise OverflowError.
- Float inputs are valid unless explicitly rejected.
- NaN/infinity are valid floats.
- TypeError depends on the actual operation and operand types.

Then provide:

1. VALID TESTS
2. INVALID TESTS
3. CORRECTED TESTS
4. MISSING TESTS
5. SECURITY REVIEW
6. FINAL TEST QUALITY SUMMARY

CODE:
{code}

ANALYSIS:
{analysis}

GENERATED TEST CASES:
{test_cases}

SECURITY REPORT:
{security_report}
"""

    response = llm.invoke(prompt)

    return response.content