import json
import yaml
from pathlib import Path
import fitz  # PyMuPDF
from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnableLambda


# Load validation rules from YAML
with open("rules.yaml", "r") as f:
    validation_rules = yaml.safe_load(f)

# Agent 1: Extract PDF Text
def extractor_agent(state):
    doc = fitz.open("C:\\Users\\HP\\OneDrive\\Desktop\\6609c53d6dbe9971ab938cc6_Car-Rental-Agreement-Template.pdf")
    full_text = "\n".join([page.get_text() for page in doc])
    return {"text": full_text}

# Agent 2: Clause Validator Agent
def clause_validator_agent(state):
    llm = ChatOllama(model="mistral")
    required_clauses = validation_rules["required_clauses"]

    prompt = f"""
Check if the following required clauses are present in this document:

Required Clauses: {required_clauses}

Document:
\"\"\"
{state['text']}
\"\"\"

Return a JSON with:
- "missing_clauses": list of clauses not found
- "found_clauses": list of clauses found
"""
    result = llm.invoke(prompt)
    parsed = json.loads(result.content[result.content.find("{"):])
    return {**state, **parsed}

# Agent 3: Compliance Checker Agent
def compliance_agent(state):
    llm = ChatOllama(model="mistral")
    formatting_issues = validation_rules["formatting_checks"]

    prompt = f"""
Review the document for formatting and red flags:
Checks: {formatting_issues}

Document:
\"\"\"
{state['text']}
\"\"\"

Return a JSON with:
- "issues_found": list of formatting/completeness issues
"""
    result = llm.invoke(prompt)
    parsed = json.loads(result.content[result.content.find("{"):])
    return {**state, **parsed}

# Agent 4: Decision Agent
def decision_agent(state):
    llm = ChatOllama(model="mistral")

    prompt = f"""
Based on the following validation results:

Missing Clauses: {state.get('missing_clauses', [])}
Issues Found: {state.get('issues_found', [])}

Decide whether the document should be APPROVED or REJECTED. 
Explain the reasoning clearly.

Return JSON:
{{
  "decision": "APPROVED" or "REJECTED",
  "reason": "..."
}}
"""
    result = llm.invoke(prompt)
    parsed = json.loads(result.content[result.content.find("{"):])
    return {"result": parsed}

# LangGraph Build
graph = StateGraph(dict)
graph.add_node("extractor", RunnableLambda(extractor_agent))
graph.add_node("validator", RunnableLambda(clause_validator_agent))
graph.add_node("compliance", RunnableLambda(compliance_agent))
graph.add_node("decider", RunnableLambda(decision_agent))

graph.set_entry_point("extractor")
graph.add_edge("extractor", "validator")
graph.add_edge("validator", "compliance")
graph.add_edge("compliance", "decider")
graph.set_finish_point("decider")
graph.add_edge("decider", END)

app = graph.compile()
final_output = app.invoke({})

# Save output
Path("output").mkdir(exist_ok=True)
with open("output/result.json", "w") as f:
    json.dump(final_output["result"], f, indent=4)

print("Validation completed. See output/result.json")
