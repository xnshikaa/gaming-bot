from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

# Allow all origins for now (secure it later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulated uptime
start_time = time.time()

@app.get("/status")
def get_status():
    return {
        "players": {
            "active": 123,
            "inactive": 45,
            "total": 168
        },
        "bot_size": "512MB",
        "db_status": "Live",
        "uptime_seconds": int(time.time() - start_time),
        "sessions_today": 18,
        "quizzes_played": 204,
        "winner": {
            "name": "John Doe",
            "prize": 1500
        },
        "current_pool": 2900,
        "time_left": "00:04:23"
    }
