# How to Run Your Flask Translator App

## Your project structure must look like this:

```
translator-flask/
├── app.py                ← your Flask server (backend)
├── requirements.txt      ← list of libraries to install
├── HOW-TO-RUN.md         ← this guide
└── templates/
    └── index.html        ← your frontend (HTML/CSS/JS)
```

WHY a templates/ folder?
Flask has a rule: HTML files must go inside a folder called "templates/"
so Flask can find and serve them using render_template().

---

## Step 1 — Open your project in VS Code

File → Open Folder → select translator-flask folder

---

## Step 2 — Open the terminal

Press Ctrl + backtick (`) in VS Code

---

## Step 3 — Install the required libraries

```bash
pip install -r requirements.txt
```

This reads requirements.txt and installs Flask, flask-cors, and requests.
You only need to do this ONCE.

---

## Step 4 — Run the Flask server

```bash
python app.py
```

You should see:
```
==================================================
  LinguaSwift Flask Server Starting...
  Open: http://localhost:5000
  Health check: http://localhost:5000/health
==================================================
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

---

## Step 5 — Open the app

Open your browser and go to:
```
http://localhost:5000
```

Your translator app will open — but this time it goes through Flask!

---

## How to test the backend directly

Open a new terminal tab and run:
```bash
curl -X POST http://localhost:5000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello", "source": "en", "target": "ur"}'
```

You should get back:
```json
{
  "success": true,
  "translation": "ہیلو",
  "source": "en",
  "target": "ur",
  "original": "Hello"
}
```

This proves your Flask backend is working correctly!

---

## What happens when you translate (full flow):

1. You type "Hello" and click Translate
2. JavaScript sends POST request to http://localhost:5000/translate
3. Flask receives it (app.py runs the translate() function)
4. Flask calls MyMemory API using Python requests library
5. MyMemory returns {"translatedText": "ہیلو"}
6. Flask packages it and returns {"success": true, "translation": "ہیلو"}
7. JavaScript receives it and displays "ہیلو" on screen

---

## Common errors and fixes:

| Error | Fix |
|---|---|
| "Module not found: flask" | Run: pip install -r requirements.txt |
| "Address already in use" | Change port=5000 to port=5001 in app.py |
| "Could not connect to server" | Make sure you ran python app.py first |
| Page not found (404) | Make sure index.html is inside templates/ folder |

---

## How to commit this to GitHub

```bash
git add .
git commit -m "Added Flask backend for translator app"
git push
```
