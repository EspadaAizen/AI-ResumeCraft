# 🧠 AI ResumeCraft

Create, edit, and polish resumes with AI.  
Supports:
- 📄 Upload & edit JSON resumes
- ✍️ Rewrite bullet points with AI
- 👀 Resume preview in app
- 📥 Download as JSON or PDF

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
