import sqlite3

def init_db():
    conn = sqlite3.connect("inspections.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inspections (
            id INTEGER PRIMARY KEY,
            license_plate TEXT,
            date TEXT,
            result TEXT,
            notes TEXT
        )
    """)
    conn.commit()
    conn.close()
