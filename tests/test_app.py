# STEP-4: regression tests of all features available on this branch.
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_extract_email():
    r=client.post("/process",json={"message":"Refund request from sara@example.com for 2026-11-04"})
    assert r.status_code==200
    assert r.json()["data"]["customer_email"]=="sara@example.com"
    assert r.json()["data"]["request_category"]=="refund"
    assert r.json()["data"]["requested_date"]=="2026-11-04"
def test_invalid_request():
    assert client.post("/process",json={"message":""}).status_code==422
def test_review_when_missing_customer():
    r=client.post("/process",json={"message":"Please help me"})
    assert r.json()["review_required"] is True
