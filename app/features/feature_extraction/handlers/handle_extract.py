# Handler: extraction -> typed validation -> review-routing service.
from app.features.feature_extraction.services.service_extract_email import extract_email
from app.features.feature_extraction.services.service_validate_fields import validate_fields
from app.features.feature_extraction.services.service_review import route_review
def handle_extract(message:str)->dict:
    return route_review(validate_fields(extract_email(message)))
