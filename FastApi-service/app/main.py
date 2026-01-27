from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Hello from my first microservice"}

@app.get("/info")
def info():
    return {
        "service": "demo-microservice",
        "version": "1.0.0"
    }
