from fastapi import FastAPI
from app.router.generate_router import router as generate_quiz_router
from app.router.generate_router import router as chat_router

app = FastAPI(docs_url="/", redoc_url="/redoc")

app.include_router(generate_quiz_router)
app.include_router(chat_router)
