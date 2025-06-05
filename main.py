import google.generativeai as genai
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Gemini API setup
GEMINI_API_KEY = "AIzaSyC39MbBHOc88knqC0zSU-IAh5si30MJKwY"
genai.configure(api_key=GEMINI_API_KEY)

# Google Docs API setup
DOCS_CREDS_FILE = "ai-workflow-agent-4da76cb57fb0.json"
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file"
]
creds = service_account.Credentials.from_service_account_file(DOCS_CREDS_FILE, scopes=SCOPES)
docs_service = build("docs", "v1", credentials=creds)
drive_service = build("drive", "v3", credentials=creds)

def summarize_text(text):
    # model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

    # print("Available models:")
    # List all available models and their supported generation methods
    # This is useful for debugging and understanding what models are available
    # for m in genai.list_models():
    #     print(m.name, m.supported_generation_methods)

    response = model.generate_content(f"Summarize this:\n{text}")
    return response.text

def write_to_google_doc(summary):
    doc = docs_service.documents().create(body={"title": "AI Summary"}).execute()
    doc_id = doc["documentId"]

    # write the summary to the document
    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={
            "requests": [
                {"insertText": {"location": {"index": 1}, "text": summary}}
            ]
        }
    ).execute()

    # Share the doc with the user
    drive_service.permissions().create(
        fileId=doc_id,
        body={"type": "user", "role": "writer", "emailAddress": "ai-workflow-agent@ai-workflow-agent.iam.gserviceaccount.com"},
        fields="id"
    ).execute()
    
    print(f"✅ Summary written: https://docs.google.com/document/d/{doc_id}")

if __name__ == "__main__":
    raw_text = input()
    #raw_text = """Your text goes here. Replace this string with whatever you want to summarize."""
    summary = summarize_text(raw_text)
    print("\n🧠 Gemini Summary:\n", summary)
    write_to_google_doc(summary)
