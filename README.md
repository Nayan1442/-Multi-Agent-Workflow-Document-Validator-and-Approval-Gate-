# 📑 Multi-Agent-Workflow-Document-Validator-and-Approval-Gate

This project builds a multi-agent system using [LangGraph](https://github.com/langgraph-ai/langgraph) and [Ollama](https://ollama.com) that can **analyze legal/business documents**, validate their structure and content based on custom rules, and automatically decide whether the document should be **approved or rejected**, along with a clear reason.

---

## 🎯 Goals

1. ✅ **Extract and validate required legal clauses** from a PDF document  
2. ✅ **Check for formatting issues**, missing elements (e.g., signatures, dates), and other red flags  
3. ✅ **Make an automated decision**: APPROVE or REJECT the document, with reasoning

---

## 🧠 How It Works

The system uses a **LangGraph agent workflow**:

| Step | Agent | Role |
|------|-------|------|
| 1️⃣ | `extractor_agent` | Extracts full text from the PDF |
| 2️⃣ | `clause_validator_agent` | Checks presence of required clauses from `rules.yaml` |
| 3️⃣ | `compliance_agent` | Reviews formatting and completeness issues |
| 4️⃣ | `decision_agent` | Decides to APPROVE or REJECT based on the results |

---

## 📁 Project Structure
.
├── main.py # Main LangGraph workflow
├── rules.yaml # YAML file defining validation rules
├── output/
│ └── result.json # Final approval decision and reasoning
└── README.md # You're here!


---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com) installed and running
- Model pulled (e.g., `mistral`):
  ollama run mistral

# Installation:
# 1. Clone the repository
git clone https://github.com/Nayan1442/-Multi-Agent-Workflow-Document-Validator-and-Approval-Gate-.git
cd Multi-Agent-Workflow-Document-Validator-and-Approval-Gate

# 2. Create a virtual environment
- python -m venv venv
- source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# Run the System
Place your PDF file at the correct path in main.py:
fitz.open("C:\\path\\to\\your\\document.pdf")

# Run the main script:
python main.py

# View the result:
output/result.json










