# Handler: extraction, typed validation, review and reproducible fixture evaluation.
from app.features.feature_extraction.services.service_extract_email import extract_email
from app.features.feature_extraction.services.service_validate_fields import validate_fields
from app.features.feature_extraction.services.service_review import route_review
from app.features.feature_extraction.services.service_evaluate import evaluate_fixtures
def handle_extract(message:str)->dict:
    outcome=route_review(validate_fields(extract_email(message)))
    outcome["evaluation"]=evaluate_fixtures()
    return outcome
