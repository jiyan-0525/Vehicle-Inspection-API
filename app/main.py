from fastapi import FastAPI
from .database import init_db
import sqlite3
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi import Form

app = FastAPI()
init_db()
@app.get("/form", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
        <body>
            <h2>Add Inspection Record</h2>
            <form action="/inspections" method="post">
                License Plate: <input name="license_plate"><br>
                Date: <input name="date"><br>
                Result: <input name="result"><br>
                Notes: <input name="notes"><br>
                <input type="submit">
            </form>
        </body>
    </html>
    """

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
def add_inspection(
    license_plate: str = Form(...),
    date: str = Form(...),
    result: str = Form(...),
    notes: str = Form(...)
):
    conn = sqlite3.connect("inspections.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO inspections (license_plate, date, result, notes) VALUES (?, ?, ?, ?)",
        (license_plate, date, result, notes)
    )
    conn.commit()
    conn.close()
    return {"message": "Record added successfully"}

