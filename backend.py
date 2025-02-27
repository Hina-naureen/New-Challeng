from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI Backend is Running!"}

@app.get("/data")
def get_data():
    return {"data": [10, 20, 30, 40, 50]}