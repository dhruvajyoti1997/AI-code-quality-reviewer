# AI Code Quality Reviewer (LangGraph + LlamaIndex + HITL)

## 📌 Overview

This project is an **AI-powered code quality reviewer** designed to analyze Java repositories.

It evaluates the overall **code quality and risk level** and classifies it into:

* **LOW** – Code is acceptable and production-ready
* **MEDIUM** – Code needs refactoring or improvements
* **HIGH** – Major design, security, or architectural issues detected

The system is **deterministic, explainable, and human-aware**, making it suitable for real-world engineering teams.

---

## 🧠 Why This Project Exists

Traditional AI code reviewers:

* Often behave like black boxes
* Lack workflow control
* Do not understand *why* a developer wrote code a certain way

This project solves that by combining:

* **LangGraph** → Workflow orchestration & decision enforcement
* **LlamaIndex** → Semantic code context retrieval
* **LLMs** → Code reasoning and classification
* **Human-in-the-Loop (HITL)** → Developer intent & justification

---

## 🏗️ High-Level Architecture

```
GitHub Repo
    ↓
Fetch Java Files (GitHub API)
    ↓
LlamaIndex (Semantic Context Retrieval)
    ↓
LLM Code Analysis
    ↓
Risk Classification (LOW / MEDIUM / HIGH)
    ↓
[If MEDIUM or HIGH]
    → Human-in-the-Loop (Developer Intent)
    → Re-analysis with Intent
    → Final Classification
```

---

## 🧩 Core Concepts

### 1️⃣ LangGraph (Workflow Orchestrator)

* Controls **states, transitions, and decisions**
* Ensures:

  * HITL is triggered only when required
  * Workflow is deterministic
  * Results are auditable

### 2️⃣ LlamaIndex (Context Engine)

* Understands relationships across files
* Retrieves relevant code sections
* Prevents shallow file-by-file analysis

### 3️⃣ Human-in-the-Loop (HITL)

* Activated only for **MEDIUM or HIGH risk**
* Allows developers to explain:

  * Design trade-offs
  * Performance constraints
  * Business-driven decisions
* Re-analysis respects justified intent

---

## 📁 Project Structure

```
ai-code-reviewer/
│
├── app/
│   ├── main.py                     # Entry point
│   │
│   ├── graph/
│   │   ├── state.py                # LangGraph state definition
│   │   └── workflow.py             # Workflow orchestration
│   │
│   ├── nodes/
│   │   ├── fetch_github_code.py    # Fetch Java files from GitHub
│   │   ├── retrieve_context.py     # LlamaIndex context retrieval
│   │   ├── analyze_code.py         # LLM analysis (intent-aware)
│   │   ├── classify_risk.py        # LOW / MEDIUM / HIGH classification
│   │   └── human_loop.py           # Human-in-the-loop node
│   │
│   ├── github/
│   │   └── github_client.py        # GitHub API wrapper
│   │
│   ├── prompts/
│   │   ├── analysis_prompt.txt
│   │   ├── classification_prompt.txt
│   │   └── hitl_prompt.txt
│   │
│   ├── llm/
│   │   └── llm_provider.py         # LLM initialization
│   │
│   └── utils/
│       └── parser.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Prerequisites

* Python **3.10+**
* GitHub account (public or private repo)
* OpenAI API key (or replaceable with Ollama later)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/ai-code-reviewer.git
cd ai-code-reviewer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-key

GITHUB_OWNER=your-github-username
GITHUB_REPO=your-repo-name
GITHUB_BRANCH=main
GITHUB_TOKEN=ghp_xxxxxx   # Optional (required for private repos)
```

---

## ▶️ How to Run

```bash
python app/main.py
```

### Possible Outcomes

* **LOW** → Process ends automatically
* **MEDIUM / HIGH** → You will be prompted to explain your design intent

Example:

```
⚠️ HUMAN REVIEW REQUIRED ⚠️
Current Risk: MEDIUM

Explain WHY this design was chosen:
> Inventory updates are async to avoid order latency under peak load
```

The system will re-analyze and produce a **final verdict**.

---

## 📊 Output Example

```
FINAL RESULT
Risk Level: MEDIUM
```

---

## 🧪 Supported Use Cases

* Direct pushes without PR/MR
* Monorepos with deep folder structures
* Microservice architectures
* Order–Inventory / Saga patterns

---

## 🧠 Design Principles

* **Deterministic workflows over autonomous agents**
* **Human-in-the-loop only when necessary**
* **Separation of concerns** (flow vs context vs reasoning)
* **Auditability & explainability**

---

## 🧑‍💻 Maintainer Notes

This project is intentionally designed to be:

* Interview-presentable
* Production-extendable
* Architecture-focused

> **LangGraph enforces policy, LlamaIndex provides context, LLMs reason, and humans provide intent.**

---
<img width="1335" height="772" alt="architecture-diagram" src="https://github.com/user-attachments/assets/e4cb4bf6-aaaa-48b8-8729-5e63bbd5bd06" />

