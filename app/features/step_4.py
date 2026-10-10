"""STEP-4 deterministic feature: Route uncertainty to review.
ICS layer: service.
Why it exists: lets readers isolate the capability from the API door.
Without it: the associated business transformation would not execute.
"""
def transform(value:str)->str:
    """Use only synthetic data and return a bounded string result."""
    return "review" if len(value.split())<3 else "accepted"
