from fastapi import FastAPI, HTTPException
from db import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running successfully!"}

@app.get("/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM FixyDB.Users")  # example table
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@app.post("/add_user")
def add_user(name: str, email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO FixyDB.users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User added successfully"}


