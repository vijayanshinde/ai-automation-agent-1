# ai-automation-agent-1
#  AI Automation Agent (FastAPI + Groq + Azure SQL)

This project implements a production‑style **AI Automation Agent** capable of:
- Understanding natural‑language requests  
- Classifying the task (summarization, extraction, rewriting, general LLM)  
- Generating intelligent responses using **Groq Llama‑3.1 models**  
- Logging all interactions into **Azure SQL Database**  
- Exposing the entire workflow through a **FastAPI microservice**

This system demonstrates how to build **deployable AI microservices**, not just notebook prototypes — ideal for real‑world automation, enterprise workflows, and AI‑powered backend services.

---

##  Features

### **1. Agentic Task Classification**
A lightweight decision engine automatically detects the user’s intent:
- Summarization  
- Information extraction  
- Email rewriting  
- General LLM reasoning  

### **2. Groq LLM Integration**
Uses Groq’s ultra‑fast Llama‑3.1 models for:
- Summaries  
- JSON extraction  
- Professional email rewrites  
- Explanations and reasoning  

### **3. Azure SQL Logging**
Every request and response is stored in a cloud database:
- User input  
- Detected task type  
- LLM output  
- Timestamp  

This enables analytics, auditing, and workflow monitoring.

### **4. FastAPI Microservice**
A clean, modern API with:
- `POST /run_agent` endpoint  
- Automatic Swagger UI at `/docs`  
- JSON request/response format  

### **5. Jupyter Notebook Development**
The notebook **aiagent1.ipynb** contains:
- Environment setup  
- Database connection  
- Table creation  
- Agent logic  
- LLM testing  
- End‑to‑end pipeline validation  

---

##  Architecture Overview

User Request
↓
FastAPI Endpoint (/run_agent)
↓
Agent Logic (task classification)
↓
Groq LLM API (Llama‑3.1)
↓
Azure SQL Logging (ai_agent_logs table)
↓
JSON Response to Client


---

##  Project Structure

.
├── aiagent1.ipynb           # Development notebook with full pipeline
├── app.py                   # FastAPI microservice
├── README.md                # Project documentation
├── .env                    # Environment variables (not included in repo)
└── requirements.txt         # Python dependencies (optional)


---

##  Setup Instructions

### **1. Clone the repository**
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```



### **2. Create a virtual environment**
```bash
conda create -n aiagent python=3.10
conda activate aiagent
```


### **3. Install dependencies**
```bash
pip install fastapi uvicorn python-dotenv sqlalchemy pyodbc requests
```



### **4. Create a .env file**
```bash
GROQ_API_KEY=your_groq_key
AZURE_SQL_CONNECTION_STRING=Driver={ODBC Driver 18 for SQL Server};Server=tcp:<your-server>.database.windows.net,1433;Database=<your-db>;Uid=<your-user>;Pwd=<your-password>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;

```
