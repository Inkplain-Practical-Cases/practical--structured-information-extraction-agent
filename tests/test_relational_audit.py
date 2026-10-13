"""Test SQLite extraction API event relationship and FK integrity."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit
def test_extraction_api_audit(tmp_path):
    path=str(tmp_path/"extraction.sqlite3")
    rid=provider_record_request_audit("POST","/process",200,5.0,path)
    with sqlite3.connect(path) as conn:
        assert conn.execute("SELECT COUNT(*) FROM extraction_api_requests WHERE id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("SELECT COUNT(*) FROM extraction_api_events WHERE request_id=?",(rid,)).fetchone()[0]==1
        assert conn.execute("PRAGMA foreign_key_check").fetchall()==[]
