# Evaluate deterministic fixtures and expose total/correct counts.
from app.features.feature_extraction.services.service_extract_email import extract_email
from app.features.feature_extraction.services.service_validate_fields import validate_fields
from app.features.feature_extraction.services.service_review import route_review

def evaluate_fixtures()->dict:
    fixtures=[("Refund my order; contact sara@example.com on 2026-11-04","refund",False),("Please help with my account","support",True),("Booking for omar@example.com on 2026-12-05","booking",False)]
    cases=[]
    for message,expected_intent,expected_review in fixtures:
        output=route_review(validate_fields(extract_email(message)))
        ok=output["data"]["request_category"]==expected_intent and output["review_required"]==expected_review
        cases.append({"intent":expected_intent,"passed":ok})
    return {"total":len(cases),"passed":sum(c["passed"] for c in cases),"cases":cases}
