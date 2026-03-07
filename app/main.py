from fastapi import FastAPI

app = FastAPI(
    title="Daily Diary API",
    description="Track daily learning and productivity",
    version="1.0"
)


@app.get("/")
def health_check():
    return {"status": "Diary API running"}