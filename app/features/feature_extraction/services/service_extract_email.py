# Offline provider: deterministic synthetic email-to-fields extraction, no model credentials.
import re
from datetime import datetime

def extract_email(message: str) -> dict:
    # Data is deliberately synthetic; this adapter can later be replaced by an LLM.
    email = re.search(r"\b([A-Za-z][\w.+-]*)@([A-Za-z][\w.-]*\.[A-Za-z]{2,})\b", message)
    date = re.search(r"\b\d{4}-\d{2}-\d{2}\b", message)
    text = message.lower()
    category = "refund" if "refund" in text else "booking" if "booking" in text else "support" if "help" in text or "support" in text else "unknown"
    return {"customer_email": email.group(0) if email else None, "request_category": category, "requested_date": date.group(0) if date else None}
