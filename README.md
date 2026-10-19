# Vehicle Inspection API

A REST API for managing vehicle inspection records.
Built with Python, FastAPI and SQLite.

## Features
- Add vehicle inspection records
- Query inspection history by license plate

## Technologies
- Python
- FastAPI
- SQLite

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Open browser: http://localhost:8000/docs

DigitcalOcean: http://46.101.164.165:8000/docs
