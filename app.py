from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routers import index, upload, analyze

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(index.router)
app.include_router(upload.router)
app.include_router(analyze.router)

if __name__ == "__main__":
    uvicorn.run("app:app", host='0.0.0.0', port=8000, reload=True)
