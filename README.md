
#  AI Automation Agent (FastAPI + Groq + Azure SQL)

This project implements a production‑style **AI Automation Agent** capable of:
- Understanding natural‑language requests  
- Classifying the task (summarization, extraction, rewriting, general LLM)  
- Generating intelligent responses using **Groq Llama‑3.1 models**  
- Logging all interactions into **Azure SQL Database**  
- Exposing the entire workflow through a **FastAPI microservice**

The development and testing process is documented in the Jupyter notebook **aiagent1.ipynb**, while the deployable microservice is implemented in **app.py**.

---

##  Features

### **1. Agentic Task Classification**
Automatically detects the user’s intent:
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

```
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
```

---

##  Project Structure

```
.
├── aiagent1.ipynb          # Development notebook with full pipeline
├── app.py                  # FastAPI microservice
├── README.md               # Project documentation
├── .env                    # Environment variables (not included in repo)
└── requirements.txt        # Python dependencies (optional)
```

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

### **4. Create a `.env` file**
```
GROQ_API_KEY=your_groq_key
AZURE_SQL_CONNECTION_STRING=Driver={ODBC Driver 18 for SQL Server};Server=tcp:<your-server>.database.windows.net,1433;Database=<your-db>;Uid=<your-user>;Pwd=<your-password>;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
```

---

##  Running the API

Navigate to the folder containing `app.py`:

```bash
cd "D:\Data Analytics\Machine Learning"
```

Start the server:

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

Use the interactive Swagger UI to test the agent.

---

##  Example Request (Swagger UI)

```json
{
  "text": "Summarize this text: Artificial intelligence is transforming industries..."
}
```

Example response:

```json
{
  "task_type": "summarization",
  "response": "• AI is transforming industries...\n• ..."
}
```

---

##  Azure SQL Table Schema

```
ai_agent_logs (
    id INT IDENTITY(1,1) PRIMARY KEY,
    user_input NVARCHAR(MAX),
    agent_action NVARCHAR(255),
    llm_response NVARCHAR(MAX),
    timestamp DATETIME DEFAULT GETDATE()
)
```


---

##  Future Enhancements

- Add authentication (API keys)
- Add more agent skills (sentiment, classification, SQL generation)
- Build a frontend UI
- Add analytics dashboards
- Deploy to Azure App Service
- Containerize with Docker

---

##  Author

**Vijayan Shinde **  
Master’s in Data Analytics & Decision Science  
RWTH Aachen University  

```


