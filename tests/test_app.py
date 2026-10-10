# STEP-1 exercises the typed FastAPI boundary.
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_valid_message():
    r=client.post('/process',json={'message':'Email from Sara'})
    assert r.status_code==200
    assert r.json()['status']=='accepted'
def test_empty_rejected():
    assert client.post('/process',json={'message':''}).status_code==422
