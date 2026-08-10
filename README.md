# 🌐 LinguaSwift — Language Translator Web App

A full-stack language translation web application built with **Python Flask** backend and vanilla **HTML/CSS/JavaScript** frontend, powered by the **MyMemory Translation API**.

Built as part of my **CodeAlpha Remote Internship** — 2025.

---

## 🚀 Live Demo

> Run locally by following the setup instructions below.

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
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
language-translator-flask/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── HOW-TO-RUN.md          # Detailed run guide
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

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Flask server
```bash
python app.py
```

### 4. Open in browser
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

## 👩‍💻 Author

**Eman Fatima**
- 🎓 BS Computer Science — University of Agriculture, Faisalabad (Semester 4)
- 💼 Software Development Intern — CodeAlpha (Remote)
- 🐙 GitHub: [Eman8765-coder](https://github.com/Eman8765-coder)
- 💼 LinkedIn: [www.linkedin.com/in/eman-fatima-4481913b6]

---

## 🚀 Live Demo
https://EmanFatima8765.pythonanywhere.com

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [MyMemory API](https://mymemory.translated.net/) — free translation service
- [Flask](https://flask.palletsprojects.com/) — Python web framework
- [Google Fonts — Inter](https://fonts.google.com/specimen/Inter) — typography
