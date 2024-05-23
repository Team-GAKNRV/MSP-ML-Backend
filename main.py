from fastapi import FastAPI
from api.v1 import api_router
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("API_PORT"))
    uvicorn.run(app, port=port)
