from fastapi import FastAPI

app = FastAPI()

jobs = []

@app.get("/")
def home():
    return {"message": "API works"}

@app.get("/jobs")
def get_jobs():
    return jobs

@app.post("/jobs")
def add_job(job: dict):
    jobs.append(job)
    return {"message": "Job added"}
