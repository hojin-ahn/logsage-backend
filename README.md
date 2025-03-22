
# LogSage Backend

An AI-powered FastAPI backend that receives runtime logs from the Flutter-based LogSage Alarm App, analyzes them using OpenAI GPT, and returns summarized insights.

---

## Features

- Accepts log data via REST API
- Integrates with OpenAI API for summarization
- Returns developer-friendly insights
- Easily deployable (e.g., on Render.com)
- Works seamlessly with the LogSage Alarm App

---

## Project Structure

```
logsage-backend/
├── main.py                # FastAPI app entry point
├── ai_analyzer.py         # OpenAI integration logic
├── models.py              # Pydantic request/response models
├── requirements.txt       # Dependencies
└── .env                   # Environment variables (API key etc.)
```

---

## API Endpoints

### `POST /analyze`

Accepts logs and returns an AI-generated summary.

#### Request Body:
```json
{
  "logs": "2025-03-21 10:22:33 [INFO] Alarm triggered\n2025-03-21 10:22:35 [WARNING] Incorrect answer"
}
```

#### Response:
```json
{
  "summary": "- Repeated incorrect answers\n- Alarm dismissed after timeout"
}
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/logsage-backend.git
cd logsage-backend
```

### 2. Create `.env` file

```bash
touch .env
```

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

Now visit `http://localhost:8000/docs` to test the API.

---

## Deploy to Render (Recommended)

1. Push your code to GitHub
2. Go to [https://dashboard.render.com/](https://dashboard.render.com/)
3. Click "New Web Service"
4. Connect your GitHub repo
5. Set these Render settings:

| Setting         | Value                          |
|----------------|---------------------------------|
| Build Command  | `pip install -r requirements.txt` |
| Start Command  | `uvicorn main:app --host 0.0.0.0 --port 10000` |
| Environment    | Python                         |
| Instance Plan  | Free                            |

6. Add environment variable in Render dashboard:
```
OPENAI_API_KEY = sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## `render.yaml` (Optional for Auto Deploy)

```yaml
services:
  - type: web
    name: logsage-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port 10000
    plan: free
    envVars:
      - key: OPENAI_API_KEY
        sync: false
```

---

## AI Prompt Template (`ai_analyzer.py`)

```python
prompt = f"""
You are an expert in software log analysis.

Analyze the following Flutter app logs and summarize:
1. Any errors or warning patterns.
2. Performance issues or delays.
3. Suggestions to improve code or UX.

Logs:
{log_text}

Respond in bullet points.
"""
```

---

## Dependencies (`requirements.txt`)

```
fastapi
uvicorn
openai
python-dotenv
```

---

## Security Note

Never commit `.env` or real API keys to GitHub.  
Use Render or Replit’s environment variable manager instead.