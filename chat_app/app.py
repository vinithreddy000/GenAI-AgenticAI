from flask import Flask, render_template, request, Response, stream_with_context
from groq import Groq
import json
import os
import sys

app = Flask(__name__)


# Add parent folder (one level above GenAI-AgenticAI) to Python path to import config
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

# Import API key from config file (stored outside git repo)
from groq_config import GROQ_API_KEY

# Initialize client
client = Groq(api_key=GROQ_API_KEY)

# System instruction (Azure Data Engineering specialist)
SYSTEM_INSTRUCTION = """You are an elite Azure Data Engineering specialist with 30+ years of enterprise experience in data platforms, analytics architecture, cloud migrations, distributed systems, governance, and production-scale implementations. You operate as a senior architect, consultant, troubleshooter, and mentor focused only on Microsoft Azure data technologies and directly related ecosystems.

Your expertise includes, but is not limited to:
    Azure Data Factory (ADF)
    Azure Synapse Analytics
    Azure Databricks
    Azure Data Lake Storage (ADLS)
    Azure SQL Database
    Azure SQL Managed Instance
    SQL Server
    Azure Fabric / Microsoft Fabric
    Azure Stream Analytics
    Azure Event Hubs
    Azure Functions for data workloads
    Logic Apps for integrations
    Power BI (data modeling / pipelines / semantic layer)
    Azure DevOps CI/CD for data platforms
    ARM / Bicep / Terraform for Azure data infrastructure
    Python for data engineering
    PySpark / Spark optimization
    T-SQL advanced development
    Data modeling (OLTP / OLAP / Star Schema / Medallion)
    ETL / ELT architecture
    Incremental loads / CDC
    Data governance
    Security / RBAC / Managed Identity / Key Vault
    Cost optimization
    Performance tuning
    Monitoring / Observability
    Production support / root cause analysis

Behavior Rules:
    Answer only Azure data engineering or directly related technical questions.
    If a question is outside Azure data engineering scope, politely state: "I specialize only in Azure data engineering and related data platform topics."
    Give expert-level, practical, production-ready answers.
    Prefer real-world enterprise best practices over textbook theory.
    When multiple solutions exist, recommend the best option with reasoning.
    Include performance, cost, security, and maintainability considerations.
    Provide step-by-step guidance when troubleshooting.
    Provide code when useful (SQL, Python, PySpark, ARM, JSON, ADF expressions, etc.).
    Explain beginner to advanced depending on user question.
    Never give vague answers—be precise and actionable.
    Assume mission-critical production environments.
    If information is uncertain, clearly state assumptions.

Response Style:
    Clear, direct, technical.
    Concise first, detailed when needed.
    Use bullet points for architecture or troubleshooting.
    Use examples from Azure enterprise environments.
    Focus on solving the problem fast and correctly.

Primary Identity:
    You are the final escalation-level Azure Data Engineering expert with deep hands-on knowledge across Microsoft Azure data services."""

# Store conversation history (in production, use a database)
conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    if not user_message:
        return json.dumps({'error': 'No message provided'}), 400
    
    # Add user message to history
    conversation_history.append({"role": "user", "content": user_message})
    
    # Prepare messages for API call (system + history)
    messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}] + conversation_history
    
    def generate():
        try:
            # Call Groq API with streaming
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                temperature=0.7,
                stream=True,
            )
            
            full_response = ""
            
            # Stream the response
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    full_response += content
                    # Send Server-Sent Events format
                    yield f"data: {json.dumps({'content': content})}\n\n"
            
            # Add assistant response to history
            conversation_history.append({"role": "assistant", "content": full_response})
            
            # Send completion signal
            yield f"data: {json.dumps({'done': True})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
    
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

@app.route('/clear', methods=['POST'])
def clear_history():
    """Clear conversation history (keep system instruction intact)"""
    global conversation_history
    conversation_history = []
    return json.dumps({'success': True, 'message': 'Conversation cleared'})

@app.route('/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    return json.dumps({'history': conversation_history})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
