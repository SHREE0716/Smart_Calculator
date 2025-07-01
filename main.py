from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Allow all CORS for dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (your frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")


# ✅ This fixes the 404 — define the endpoint!
class CalculationInput(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/calculate")
def calculate(data: CalculationInput):
    if data.operation == "add":
        result = data.num1 + data.num2
    elif data.operation == "subtract":
        result = data.num1 - data.num2
    elif data.operation == "multiply":
        result = data.num1 * data.num2
    elif data.operation == "divide":
        if data.num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = data.num1 / data.num2
    else:
        result = "Invalid operation"
    return {"result": result}
