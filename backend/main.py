import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from pydantic import BaseModel

from test_builder import build_test_file
from test_validator import validate_test_file
from graph.workflow import testpilot_graph


app = FastAPI(
    title="TestPilot AI",
    description="Multi-Agent AI Software Testing Platform",
    version="1.0.0"
)


# Allow the Next.js frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def root():
    return {
        "message": "TestPilot AI API is running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze_code(request: CodeRequest):

    result = testpilot_graph.invoke({
        "code": request.code,
        "result": ""
    })

    raw_result = result["result"]

    try:
        data = json.loads(raw_result)

    except json.JSONDecodeError:

        data = {
            "analysis": raw_result,
            "test_cases": [],
            "security": "Unable to parse structured response"
        }

    # Build and validate the generated test file
    test_file = build_test_file(
        request.code,
        data.get("test_cases", [])
    )

    validated_test_file = validate_test_file(test_file)

    return {
        "analysis": data.get("analysis", ""),
        "test_cases": data.get("test_cases", []),
        "security": data.get("security", "None"),
        "validated_tests": validated_test_file
    }


@app.post("/generate-tests")
def generate_tests(request: CodeRequest):

    result = testpilot_graph.invoke({
        "code": request.code,
        "result": ""
    })

    data = json.loads(result["result"])

    test_file = build_test_file(
        request.code,
        data.get("test_cases", [])
    )

    test_file = validate_test_file(test_file)

    return Response(
        content=test_file,
        media_type="text/x-python",
        headers={
            "Content-Disposition": 'attachment; filename="test_generated.py"'
        }
    )