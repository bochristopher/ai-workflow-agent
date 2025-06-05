import openai
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Load your Gemini API key and Google credentials here
GEMINI_API_KEY = 'your-gemini-api-key'
DOCS_CREDS_FILE = 'credentials.json'

def summarize_text(text):
    openai.api_key = GEMINI_API_KEY
    response = openai.ChatCompletion.create(
        model="gemini-pro",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    return response['choices'][0]['message']['content']

def write_to_google_doc(summary):
    creds = service_account.Credentials.from_service_account_file(DOCS_CREDS_FILE, scopes=["https://www.googleapis.com/auth/documents"])
    service = build('docs', 'v1', credentials=creds)
    doc = service.documents().create(body={'title': 'AI Summary'}).execute()
    doc_id = doc['documentId']
    service.documents().batchUpdate(documentId=doc_id, body={
        'requests': [{
            'insertText': {
                'location': {'index': 1},
                'text': summary
            }
        }]
    }).execute()
    print(f"Summary written to document: https://docs.google.com/document/d/{doc_id}")

# Example usage
if __name__ == "__main__":
    input_text = "This is a long article or meeting notes..."
    summary = summarize_text(input_text)
    write_to_google_doc(summary)
