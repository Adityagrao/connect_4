from fastapi import FastAPI
from src.api import api_router
from functools import lru_cache
from config import Settings
import uvicorn


app = FastAPI(title="Connect 4 Demo",
              description="API's to Create and Play a game of Connect 4")


@lru_cache()
def get_settings():
    if Settings().connection_string is None:
        raise SystemExit("Configure DB before running")
    return Settings()


app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
