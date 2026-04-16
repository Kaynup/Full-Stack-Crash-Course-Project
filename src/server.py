import mysql.connector
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel, ValidationError
# print(fastapi.__version__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Payload(BaseModel):
    first_name: str
    last_name: str
    email: str
    job_title: Optional[str] = None
    salary: Optional[float] = None

def get_connection():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="intern_project"
        )

@app.get("/status")
def home():
    return {"message":"API is live"}

@app.post("/register")
def register(pl: Payload):
    con = get_connection()
    cur = con.cursor()

    query = """
    INSERT INTO employees 
    (first_name, last_name, email, hire_date, job_title, salary)
    VALUES (%s, %s, %s, CURDATE(), %s, %s)
    """

    cur.execute(query, (
        pl.first_name,
        pl.last_name,
        pl.email,
        pl.job_title,
        pl.salary
    ))

    con.commit()

    cur.close()
    con.close()

    return {
        "message": "Success!"
    }

# Verification
try:
    pl = Payload(
        first_name="Punyak",
        last_name="User",
        email="punyak@test.com",
        job_title="Backend Dev",
        salary=50000
    )
    print(pl)
except ValidationError as e:
    print(e.json())