# 🧠 AI Workflow Agent with Gemini + Google Docs

This tool summarizes text using Google's Gemini API and automatically writes the result into a Google Doc using the Google Docs API.

🚀 It also shares the generated document with your Gmail address automatically — no more copy-paste or manual permissions!

---

## ✅ Features

- Summarize any text using `gemini-1.5-flash-latest`
- Automatically create and write to a new Google Doc
- Share the Doc with your personal Gmail account

---

## 🔧 Setup Instructions

### 1. Clone or download this repo and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Add Your Credentials

Place your `credentials.json` file in the root of the project.  
Rename it to: `ai-workflow-agent-4da76cb57fb0.json`

You can generate this from the [Google Cloud Console](https://console.cloud.google.com/).

### 3. Set Your Gmail

In `main_combined.py`, update this line:
```python
your_email = "your.email@gmail.com"
```

---

## ▶️ Run It

```bash
python main_combined.py
```

You’ll be prompted to paste in text, and the program will:
1. Summarize it
2. Create a Google Doc
3. Share it with your Gmail address

---

## 💡 Tip

To confirm sharing worked, open your **Shared with me** section in [Google Drive](https://drive.google.com/drive/shared-with-me).

---

## 📄 License

MIT License

---

## 🛠 Troubleshooting & Debugging

### 🔒 1. “Request had insufficient authentication scopes”
✅ Make sure you include **all of these scopes** when creating your service account credentials:
- https://www.googleapis.com/auth/documents
- https://www.googleapis.com/auth/drive
- https://www.googleapis.com/auth/drive.file

If you still get 403 errors, delete and **recreate your `credentials.json`** from Google Cloud Console **after adding the correct scopes**.

---

### 🕵️‍♂️ 2. “I can’t see the Google Doc in my Drive”
✅ Docs created by the service account are **not owned by your Gmail account**. You must either:
- Share them manually
- Use the built-in script functionality to auto-share with your Gmail

---

### 🚫 3. “Request Access” error even after creating the doc
✅ This means the service account created the doc, but it wasn’t shared. Use the script’s sharing function, or manually use Google’s [Drive API Explorer](https://developers.google.com/drive/api/v3/reference/permissions/create#try-it).

---

### 🧯 4. Gemini model error: “model not found or unsupported”
✅ Use `"models/gemini-1.5-flash-latest"` — it’s reliable and supported.  
Avoid `"gemini-pro"` unless you confirm it's available via `genai.list_models()`.

---

### ⏳ 5. “429: You exceeded your current quota”
✅ You hit the free-tier rate limit for Gemini API. Try:
- Switching to `"gemini-1.5-flash-latest"` (lower cost)
- Waiting a few minutes
- Upgrading your quota in the [Gemini API Console](https://makersuite.google.com/app/apikey)

---

### 🧪 6. No "Try It" in Google API Docs?
✅ You're probably in Incognito or not signed in. Use a regular browser tab and sign in to see the **“Try this method”** section.

---
