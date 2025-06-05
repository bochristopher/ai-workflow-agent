![AI Workflow Agent Banner](workshop_slide_final_widescreen.png)

# Build an AI Workflow Agent with Gemini + Google Docs

This project is part of a hands-on workshop that walks you through building an AI-powered assistant to summarize notes and automatically store them in Google Docs using Python, Gemini API, and the Google Docs API.

## 🔧 What You'll Build
- Summarize notes using Gemini (LLM)
- Create and edit Google Docs programmatically
- Automate your workflow with Python

---

## 🧠 Prerequisites
- Basic Python knowledge
- Google Account
- Gemini API Key
- Google Cloud Project with Docs API enabled

---

## 🛠 Tools & Setup

### Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Required Packages
```bash
pip install --upgrade pip
pip install openai google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Save Environment (Optional)
```bash
pip freeze > requirements.txt
```

### Later, to Reinstall from Requirements:
```bash
pip install -r requirements.txt
```

Set up:
1. Get a [Gemini API Key](https://makersuite.google.com/app)
2. Set up a Google Cloud project with Docs API enabled
3. Download your `credentials.json` for a service account
4. Place it in the project folder

---

## 🚀 How to Run

### 1. Summarize your text
```python
def summarize_text(text):
    openai.api_key = "your-gemini-api-key"
    response = openai.ChatCompletion.create(
        model="gemini-pro",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    return response['choices'][0]['message']['content']
```

### 2. Write to Google Docs
```python
def write_to_google_doc(summary):
    from googleapiclient.discovery import build
    from google.oauth2 import service_account

    SCOPES = ['https://www.googleapis.com/auth/documents']
    creds = service_account.Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
    docs_service = build('docs', 'v1', credentials=creds)

    doc = docs_service.documents().create(body={'title': 'AI Summary'}).execute()
    doc_id = doc['documentId']
    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': [{'insertText': {'location': {'index': 1}, 'text': summary}}]}
    ).execute()

    print(f"Document created: https://docs.google.com/document/d/{doc_id}")
```

### 3. Run It All
```python
if __name__ == "__main__":
    raw_notes = input("Paste your notes here:\n")
    summary = summarize_text(raw_notes)
    write_to_google_doc(summary)
```

---

## 🙋‍♂️ About the Instructor
**Bo Christopher Redfearn**  
Hardware Validation Engineer @ Apple  
[LinkedIn](https://linkedin.com/in/bochristopher) • [GitHub](https://github.com/bochristopher)

---

## 📄 License
MIT License
