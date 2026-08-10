# 🌐 LinguaSwift — Language Translator Web App

A full-stack language translation web application built with **Python Flask** backend and vanilla **HTML/CSS/JavaScript** frontend, powered by the **MyMemory Translation API**.

Built as part of my **AI Internship at CodeAlpha** — August 2026.

---

## 🚀 Live Demo

🔗 **[https://EmanFatima8765.pythonanywhere.com](https://EmanFatima8765.pythonanywhere.com)**

---

## 📸 Features

- 🌍 Translate text between 10+ languages instantly
- 🔊 Text-to-speech — hear the translation read aloud
- 📋 One-click copy translated text to clipboard
- ⇄ Swap source and target languages instantly
- ⚠️ Error handling for empty input, same language, and API failures
- 📱 Responsive design — works on mobile and desktop
- ⌨️ Keyboard shortcut — press **Ctrl + Enter** to translate

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, JavaScript (Vanilla) |
| Backend | Python 3, Flask |
| API | MyMemory Translation API (free) |
| Deployment | PythonAnywhere (free hosting) |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
language-translator-flask/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── Procfile               # For alternative deployment (Render)
├── .gitignore             # Files excluded from Git
├── README.md              # Project documentation
├── HOW-TO-RUN.md          # Detailed local run guide
└── templates/
    └── index.html         # Frontend (HTML + CSS + JS)
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Eman8765-coder/language-translator-flask.git
cd language-translator-flask
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Flask server
```bash
python app.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 🔄 How It Works

```
User types text
      ↓
JavaScript sends POST request to Flask (/translate)
      ↓
Flask validates input and calls MyMemory API
      ↓
MyMemory returns translated text
      ↓
Flask sends result back to browser
      ↓
JavaScript displays translation on screen
```

The frontend never talks directly to the translation API.
All requests go through the Flask backend — this is the correct
and secure way to build a full-stack web application.

---

## 🌐 Supported Languages

| Language | Code |
|---|---|
| English | en |
| Urdu | ur |
| Arabic | ar |
| French | fr |
| Spanish | es |
| German | de |
| Chinese | zh |
| Hindi | hi |
| Turkish | tr |
| Russian | ru |

---

## 📡 API Reference

This app uses the **MyMemory API** — free, no API key required.

**Endpoint used:**
```
GET https://api.mymemory.translated.net/get?q={text}&langpair={source}|{target}
```

**Flask route created:**
```
POST /translate
Content-Type: application/json
Body: { "text": "Hello", "source": "en", "target": "ur" }
```

**Response:**
```json
{
  "success": true,
  "translation": "ہیلو",
  "source": "en",
  "target": "ur",
  "original": "Hello"
}
```

---

## ☁️ Deployment

This app is deployed on **PythonAnywhere** using a Python 3.10 virtual environment.

**Live URL:** https://EmanFatima8765.pythonanywhere.com

**Deployment steps:**
1. Clone repo on PythonAnywhere via Bash console
2. Create virtualenv with Python 3.10
3. Install dependencies inside virtualenv
4. Configure WSGI file to point to Flask app
5. Set virtualenv path in Web tab
6. Reload web app

---

## 👩‍💻 Author

**Eman Fatima**
- 🎓 BS Computer Science — University of Agriculture, Faisalabad (Semester 4)
- 💼 AI Intern — CodeAlpha (Remote) · Aug 2026 – Sep 2026
- 🐙 GitHub: [Eman8765-coder](https://github.com/Eman8765-coder)
- 💼 LinkedIn: [linkedin.com/in/eman-fatima-4481913b6](https://linkedin.com/in/eman-fatima-4481913b6)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [MyMemory API](https://mymemory.translated.net/) — free translation service
- [Flask](https://flask.palletsprojects.com/) — Python web framework
- [PythonAnywhere](https://www.pythonanywhere.com/) — free Python hosting
- [Google Fonts — Inter](https://fonts.google.com/specimen/Inter) — typography
