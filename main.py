import uvicorn

from fastapi import FastAPI

from app.core.config import run_host, run_port


app = FastAPI()


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host=run_host,
        port=run_port,
        reload=True
    )
