from fastapi import FastAPI
from routes import resume

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "IT'S WORKING - FastAPI backend is running!"}

# Register resume routes
app.include_router(resume.router, prefix="/resume")
