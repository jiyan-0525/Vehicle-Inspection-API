# Vehicle Inspection API

A REST API for managing vehicle inspection records.
Built with Python, FastAPI and SQLite.

## Background
Inspired by my experience working in the automotive 
inspection industry in Germany.

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
pip install fastapi uvicorn
```

## Run
```bash
uvicorn main:app --reload
```

Open browser: http://localhost:8000/docs

## Author
42 Heilbronn student with background in automotive industry
