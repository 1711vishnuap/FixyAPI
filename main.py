from fastapi import FastAPI, HTTPException
from db import get_connection
from fastapi import FastAPI
from pydantic import BaseModel

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

class User(BaseModel):
    name: str
    email: str
    phoneno: str
    password: str

@app.post("/add_user")
def add_user(user: User):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO FixyDB.Users (fullname, email,phoneno,password) VALUES (%s, %s,%s, %s)"
        params = (user.name, user.email,user.phoneno,user.password)

        cursor.execute(query, params)
        conn.commit()

        cursor.close()
        conn.close()

        return {"message": "User added successfully"}

    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/isvalid_user")
def is_valid_user(username: str, password: str):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if user exists
        query = """
            SELECT COUNT(*) AS count
            FROM FixyDB.Users
            WHERE (PhoneNo = %s AND Password = %s)OR(Email = %s AND Password = %s)
        """
        cursor.execute(query, (username, password,username, password))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        # Convert to bit value
        return {"isValid": 1 if result["count"] > 0 else 0}

    except Exception as e:
        return {"error": str(e)}















