# Handler: validate extracted fields before responding.
from app.features.feature_extraction.services.service_extract_email import extract_email
from app.features.feature_extraction.services.service_validate_fields import validate_fields
def handle_extract(message:str)->dict:
    record=validate_fields(extract_email(message))
    return {"status":"validated","data":record}
