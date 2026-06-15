from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from routers import users_router, meals_router, tokens_router

# Automatically create the SQLite file and tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cafeteria Token System API")

# Enable CORS (Cross-Origin Resource Sharing) 
# This permits your React frontend (running on a different port) to talk to this API safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, change this to your React app's specific URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect our modular routers
app.include_router(users_router.router)
app.include_router(meals_router.router)
app.include_router(tokens_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Cafeteria Token System API! Head to /docs for the interactive UI."}