from fastapi import FastAPI

app = FastAPI(
    title="TestPilot AI",
    description="Multi-Agent AI Software Testing Platform",
    version="1.0.0"
)


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