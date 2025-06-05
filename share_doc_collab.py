# 🧠 Gemini + Google Docs Auto-Sharing Tool

import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive']

# Use service account credentials (recommended for automation)
SERVICE_ACCOUNT_FILE = 'ai-workflow-agent-4da76cb57fb0.json'  # Place your service account JSON here

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=creds)

# Step 1: Input the Google Doc ID
doc_id = input("Paste the Document ID from your Google Doc URL: ")

# Step 2: Input your Gmail
your_email = input("Enter your Gmail address to share the doc with: ")

# Step 3: Share the document
try:
    permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': your_email
    }
    result = drive_service.permissions().create(
        fileId=doc_id,
        body=permission,
        fields='id'
    ).execute()
    print("✅ Success! The document is now shared with", your_email)
    print(f"https://docs.google.com/document/d/{doc_id}")
except HttpError as error:
    print(f"❌ An error occurred: {error}")
