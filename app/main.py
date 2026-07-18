from fastapi import FastAPI
from .database import init_db
import sqlite3
from typing import Optional

app = FastAPI()
init_db()

@app.get("/")
def get_inspections(license_plate: Optional[str] = None):
    conn = sqlite3.connect("inspections.db")
    cursor = conn.cursor()

    if license_plate:
        cursor.execute("SELECT * FROM inspections WHERE license_plate = ?", (license_plate,))
    else:
        cursor.execute("SELECT * FROM inspections")

    rows = cursor.fetchall()
    conn.close()
    return {"records": rows}

@app.post("/inspections")
def add_inspection(license_plate: str, date: str, result: str, notes: str):
    conn = sqlite3.connect("inspections.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO inspections (license_plate, date, result, notes) VALUES (?, ?, ?, ?)",
        (license_plate, date, result, notes)
    )
    conn.commit()
    conn.close()
    return {"message": "记录已添加"}

