```mermaid
flowchart TD
    Start([Start])
    Start --> A[PDF Extractor Agent]
    A --> B[Clause Validator Agent]
    B --> C[Compliance Checker Agent]
    C --> D[Decision Agent]
    D --> E{Decision}
    E -->|APPROVED| F[ Approved Document]
    E -->|REJECTED| G[ Rejected with Reason]
    F --> End([End])
    G --> End



---

### ✅ Explanation of Nodes

| Node | Description |
|------|-------------|
| `Start` | Entry point of the workflow |
| `PDF Extractor Agent` | Extracts full text from the PDF |
| `Clause Validator Agent` | Checks if required clauses exist |
| `Compliance Checker Agent` | Verifies formatting issues, dates, signatures, red flags |
| `Decision Agent` | Combines validation results and makes a final decision |
| `APPROVED/REJECTED` | Based on rules and reasoning |
| `End` | Finishes the LangGraph pipeline |

---

Let me know if you want this rendered as an **image**, included in your `README.md`, or used in a Streamlit UI.
