# Azure Data Engineering AI Chat Assistant

A professional web-based chat interface powered by Groq's LLM API, specialized in Azure Data Engineering expertise.

## 🚀 Features

* **Real-time streaming responses** using Server-Sent Events (SSE)
* **Conversation history management** (maintains context across messages)
* **System instruction preservation** (expert persona is never cleared)
* **Modern, responsive UI** with gradient design
* **Code syntax highlighting** with markdown support
* **Mobile-friendly** responsive layout

## 📁 Project Structure

```
chat_app/
├── app.py                 # Flask backend with Groq API integration
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # Chat interface HTML
└── static/
    └── style.css         # Styling and animations
```

## 🛠️ Installation

### Prerequisites

* Python 3.8 or higher
* Groq API key (already included in the code)

### Steps

1. **Navigate to the project directory:**
   ```bash
   cd chat_app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Start chatting!** Ask questions about:
   * Azure Data Factory & Synapse Analytics
   * Azure Databricks & Data Lake Storage
   * SQL Server, Azure SQL, & Microsoft Fabric
   * ETL/ELT Architecture & Performance Optimization
   * Data Governance, Security & Cost Optimization

## 🔧 Configuration

### Changing the API Key

For production use, it's recommended to use environment variables:

1. **Set the environment variable:**
   ```bash
   # Linux/Mac
   export GROQ_API_KEY="your_api_key_here"
   
   # Windows CMD
   set GROQ_API_KEY=your_api_key_here
   
   # Windows PowerShell
   $env:GROQ_API_KEY="your_api_key_here"
   ```

2. **Update app.py line 8:**
   ```python
   client = Groq(api_key=os.getenv("GROQ_API_KEY"))
   ```

### Customizing the System Instruction

Edit the `SYSTEM_INSTRUCTION` variable in `app.py` (lines 11-60) to change the AI assistant's persona and expertise.

### Changing the Model

Edit line 79 in `app.py` to use a different Groq model:
```python
model="llama-3.3-70b-versatile",  # Change this
```

Available models:
* `llama-3.3-70b-versatile`
* `llama-3.1-70b-versatile`
* `mixtral-8x7b-32768`
* And more (check Groq documentation)

## 🎨 UI Features

* **Streaming responses**: See the AI's response as it's being generated
* **Message history**: Full conversation context is maintained
* **Clear chat**: Reset conversation while preserving system instruction
* **Markdown support**: Code blocks, bold, italic, and inline code
* **Auto-scrolling**: Always shows the latest message
* **Keyboard shortcuts**: 
  * `Enter` to send
  * `Shift+Enter` for new line

## 🔒 Security Notes

⚠️ **IMPORTANT**: The API key is currently hardcoded in `app.py`. For production:

1. **Never commit API keys** to version control
2. **Use environment variables** or a secrets manager
3. **Add `.env` to `.gitignore`**
4. **Implement rate limiting** to prevent abuse
5. **Add authentication** if deploying publicly

## 📝 API Endpoints

### `GET /`
Serves the main chat interface.

### `POST /chat`
Sends a message and receives a streaming response.

**Request body:**
```json
{
  "message": "How do I optimize ADF pipelines?"
}
```

**Response:** Server-Sent Events stream

### `POST /clear`
Clears the conversation history (preserves system instruction).

**Response:**
```json
{
  "success": true,
  "message": "Conversation cleared"
}
```

### `GET /history`
Retrieves the conversation history.

**Response:**
```json
{
  "history": [
    {"role": "user", "content": "..."},
    {"role": "assistant", "content": "..."}
  ]
}
```

## 🐛 Troubleshooting

### Port already in use
```bash
# Change the port in app.py line 119:
app.run(debug=True, host='0.0.0.0', port=5001)  # Use a different port
```

### Module not found
```bash
pip install --upgrade flask groq
```

### API key errors
Ensure your Groq API key is valid and has sufficient credits.

## 🚀 Deployment Options

### Local Development
Use the built-in Flask server (already configured).

### Production Deployment

1. **Gunicorn (Linux/Mac):**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

2. **Docker:**
   Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "app.py"]
   ```

3. **Cloud Platforms:**
   * AWS Elastic Beanstalk
   * Google Cloud Run
   * Azure App Service
   * Heroku

## 📚 Learn More

* [Groq API Documentation](https://console.groq.com/docs)
* [Flask Documentation](https://flask.palletsprojects.com/)
* [Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 📄 License

Free to use and modify for personal and commercial projects.

## 🤝 Contributing

Feel free to fork, enhance, and submit pull requests!

---

**Built with ❤️ using Flask, Groq API, and modern web technologies**