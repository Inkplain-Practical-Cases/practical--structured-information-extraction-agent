# Review policy: a missing customer or unknown intent requires human attention.
def route_review(record:dict)->dict:
    incomplete=record.get("customer_email") is None or record.get("request_category")=="unknown"
    return {"status":"needs_review" if incomplete else "ready","data":record,"review_required":incomplete}
