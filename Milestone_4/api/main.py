from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from orchestrator.workflow_manager import WorkflowManager

app = FastAPI(title="AI Workflow Studio")

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

manager = WorkflowManager()


@app.get("/")
def home():

    return {"status": "API Running"}


@app.post("/workflow")
def run(topic: str):

    return manager.run_workflow(topic)
