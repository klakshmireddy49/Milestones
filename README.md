# 🧠 Multi-Agent Workflow System using LangChain

## 📌 Overview

This project implements a **multi-agent orchestration framework** using LangChain, enabling intelligent task automation through collaboration between specialized agents.

The system supports a complete workflow:
**Research → Analysis → Summarization → Email Composition → Evaluation**

It integrates:

* Multi-agent communication
* Memory-based reasoning
* Tool usage (APIs)
* REST API backend
* Interactive frontend

---

## 🚀 Features

* 🤖 Multiple specialized agents (Research, Summary, Email, Evaluation, Analysis)
* 🔗 Agent orchestration and communication
* 🧠 Memory integration (individual + shared)
* 🛠 Tool integration (Calculator, Web Search, Text Cleaner)
* 🌐 REST API (Flask/FastAPI)
* 💻 Frontend interface for interaction
* 🧪 Workflow testing and evaluation

---

## 🏗 Project Structure

```
workflow_system/
├── agents/          # Agent implementations
├── api/             # Backend API
├── frontend/        # UI (HTML, CSS, JS)
├── orchestrator/    # Workflow logic
├── tools/           # Custom tools
├── utils/           # Helper functions
├── tests/           # Test cases
├── docs/            # Documentation
└── README.md
```

---

## 🧩 Milestones

* **Milestone 1** → Environment Setup & Basic Agent
* **Milestone 2** → Tool Integration & API Calling
* **Milestone 3** → Multi-Agent Orchestration & Memory
* **Milestone 4** → Workflow Automation, API & Frontend

👉 Full implementation available in:
`Milestone_4/workflow_system/`

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run API

```bash
cd workflow_system/api
python main.py
```

### Open frontend

* Open `frontend/index.html` in browser

---

## 🔄 Workflow Example

1. User submits query
2. Research Agent gathers data
3. Analysis Agent processes information
4. Summary Agent condenses results
5. Email Agent composes response
6. Evaluation Agent validates output

---

## 🧪 Testing

```bash
pytest workflow_system/tests/
```

---

## 📊 Evaluation

* Multi-agent collaboration verified
* Memory-driven decision making implemented
* Tool usage validated
* End-to-end workflow tested

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

K.LAKSHMI REDDY

---

## ⭐ Acknowledgment

Built using LangChain and modern AI agent orchestration concepts.
