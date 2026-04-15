from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, ValidationError
# print(fastapi.__version__)

app = FastAPI()

class Payload(BaseModel):
    name: str
    age: int
    desc: Optional[str] = None

@app.get("/status")
def home():
    return {"message":"API is live"}

@app.post("/register")
def payload(pl: Payload):
    return {
        "message":"Success!",
        "data":pl
        }

# Verification
try:
    pl = Payload(name="Punyak", age=20, desc="Backend Dev")
    print(pl)
except ValidationError as e:
    print(e.json())