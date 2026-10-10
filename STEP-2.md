# STEP-2 — Call offline extraction provider

## Build
A source-aligned cumulative extraction service with type checks, review routing and local fixtures through the current step.

## Run
```bash
python -m pip install -r requirements.txt
python -m pytest -q
uvicorn app.main:app --reload
```

## Diagram
Read STEP-2.crd for each Python component contract; the six-stage portal follows this exact branch.
