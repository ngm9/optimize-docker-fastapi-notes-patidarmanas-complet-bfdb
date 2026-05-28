from fastapi import FastAPI, HTTPException
from app.routers import notes
app = FastAPI()
app.include_router(notes.router)

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
