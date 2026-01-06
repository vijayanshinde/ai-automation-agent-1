from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
import sqlalchemy as sa
import urllib
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
raw_conn_str = os.getenv("AZURE_SQL_CONNECTION_STRING")
params = urllib.parse.quote_plus(raw_conn_str)

# Create SQLAlchemy engine with autocommit
engine = sa.create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}",
    isolation_level="AUTOCOMMIT"
)

# FastAPI app
app = FastAPI(title="AI Automation Agent API")

# Request model
class UserRequest(BaseModel):
    text: str

# --- Groq LLM call ---
def call_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "error" in result:
        return f"[Groq API Error] {result['error']['message']}"
    if "choices" not in result:
        return f"[Unexpected API Response] {result}"

    return result["choices"][0]["message"]["content"]

# --- Simple agent logic ---
def classify_task(user_input):
    text = user_input.lower()
    if "summarize" in text:
        return "summarization"
    if "extract" in text:
        return "extraction"
    if "email" in text or "rewrite" in text:
        return "email_rewrite"
    return "general_llm"

# --- API endpoint ---
@app.post("/run_agent")
def run_agent(request: UserRequest):
    user_input = request.text
    action = classify_task(user_input)

    # Build prompt
    if action == "summarization":
        prompt = f"Summarize the following text in 3 bullet points:\n\n{user_input}"
    elif action == "extraction":
        prompt = f"Extract key fields from this text and return them as JSON:\n\n{user_input}"
    elif action == "email_rewrite":
        prompt = f"Rewrite this email to sound professional:\n\n{user_input}"
    else:
        prompt = user_input

    # LLM call
    llm_output = call_groq(prompt)

    # Store in Azure SQL
    with engine.begin() as conn:
        conn.execute(sa.text("""
            INSERT INTO ai_agent_logs (user_input, agent_action, llm_response)
            VALUES (:user_input, :agent_action, :llm_response)
        """), {
            "user_input": user_input,
            "agent_action": action,
            "llm_response": llm_output
        })

    return {
        "task_type": action,
        "response": llm_output
    }
