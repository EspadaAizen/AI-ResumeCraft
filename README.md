# 🧠 AI ResumeCraft

> ✨ Create, edit, and polish resumes with AI — directly in your browser.  
> Build from scratch, upload existing JSON resumes, edit them visually, and download as PDF — no setup needed!

[![Streamlit](https://img.shields.io/badge/Live_App-Streamlit-blue?logo=streamlit)](https://ai-resumecraft-3zenwduk3qkwdmpsgfpbrm.streamlit.app/)
[![Python](https://img.shields.io/badge/Built_with-Python-yellow?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🌐 Live Demo
Try it instantly here:  
👉 [https://ai-resumecraft-3zenwduk3qkwdmpsgfpbrm.streamlit.app/](https://ai-resumecraft-3zenwduk3qkwdmpsgfpbrm.streamlit.app/)

---

## ✨ Features
- 📄 **Upload & Edit JSON Resumes** — Upload your resume and edit all fields in a clean UI.
- ✍️ **AI Resume Rewriter** — Rewrite your bullet points into professional, action-focused language.
- 🧩 **Resume Builder** — Create a JSON resume from scratch using form inputs.
- 👀 **In-App Preview** — See your resume in formatted view instantly.
- 📥 **Download as JSON or PDF** — Export resumes with one click.
- ⚙️ **Mock or Real AI Mode** — Works offline (mock mode) or online with OpenAI/Ollama.

---

## 📂 Structure
- `backend/` → FastAPI app
- `frontend/` → Streamlit app
- `requirements.txt` → install dependencies

## 🚀 Run locally

### 1. Clone repo
```bash
git clone https://github.com/espadaaizen/AI-ResumeCraft.git
cd AI-ResumeCraft
```

### 2. Setup virtual env
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
Frontend:
cd frontend
pip install -r requirements.txt

Backend:
cd backend
pip install -r requirements.txt
```

### 4. Run locally
```bash
Backend(fastApi):
cd backend
uvicorn main:app --reload --port 8000

Frontend (Streamlit):
cd frontend
streamlit run app.py
```
