# Handler: orchestrate a deterministic extraction adapter and return its result.
from app.features.feature_extraction.services.service_extract_email import extract_email
def handle_extract(message:str)->dict:
    return {"status":"extracted","data":extract_email(message)}
