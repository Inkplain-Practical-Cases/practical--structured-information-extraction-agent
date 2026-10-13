# STEP-5 — Evaluate extraction fixtures

## Build
A source-aligned cumulative extraction service with type checks, review routing and local fixtures through the current step.

## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

## Diagram
Read STEP-5.crd for each Python component contract; the six-stage portal follows this exact branch.

## Database (Entity) Relations
SQLite stores extraction API HTTP request/outcome metadata without source text. See STEP-5.erd and STEP-5-ERD.
