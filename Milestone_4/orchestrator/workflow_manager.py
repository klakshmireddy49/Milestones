import time

from agents.research_agent import research_agent
from agents.analysis_agent import analysis_agent
from agents.summary_agent import summary_agent
from agents.email_agent import email_agent
from agents.evaluation_agent import evaluation_agent

from utils.metrics import calculate_metrics


class WorkflowManager:

    def run_workflow(self, topic):

        start = time.time()

        steps = {}

        research = research_agent(topic)
        steps["research"] = "completed"

        analysis = analysis_agent(research)
        steps["analysis"] = "completed"

        summary = summary_agent(analysis)
        steps["summary"] = "completed"

        email = email_agent(summary)
        steps["email"] = "completed"

        evaluation = evaluation_agent(email)
        steps["evaluation"] = "completed"

        metrics = calculate_metrics(start)

        return {
            "steps": steps,
            "research": research,
            "analysis": analysis,
            "summary": summary,
            "email": email,
            "evaluation": evaluation,
            "metrics": metrics,
        }
