from fastapi import FastAPI

app = FastAPI(title="Hasan")


@app.get("/")
def root():
    return {"message": "Hello, World!"}
