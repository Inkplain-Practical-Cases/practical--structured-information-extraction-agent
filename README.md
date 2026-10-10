# Structured Information Extraction Agent

Starter FDE project: extract customer email, request category and ISO date from synthetic input. Branches STEP-1 to STEP-5 model API contracts, offline extraction, structured validation, review routing and reproducible fixture evaluation.

## Run
`python -m pip install -r requirements.txt`
`python -m pytest -q`
`uvicorn app.main:app --reload`

## Limitations
This is an offline deterministic teaching application, not a connected LLM. External model extraction, security, persistent review and customer production integrations require additional engineering.
