from fastapi import FastAPI
from database import init_db
import sqlite3

app = FastAPI()
init_db()

# 查询某辆车的所有检测记录
@app.get("/inspections/{license_plate}")
def get_inspections(license_plate: str):
    conn = sqlite3.connect("inspections.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM inspections WHERE license_plate = ?",
        (license_plate,)
    )
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

