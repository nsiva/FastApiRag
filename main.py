# main.py
from fastapi import FastAPI
from routers.user_guide_router import router as user_guide_router

app = FastAPI()

app.include_router(user_guide_router)

@app.get("/")
async def root():
    return {"message": "User Guide API"}