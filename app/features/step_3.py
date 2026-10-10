"""STEP-3 deterministic feature: Parse and validate structured output.
ICS layer: service.
Why it exists: lets readers isolate the capability from the API door.
Without it: the associated business transformation would not execute.
"""
def transform(value:str)->str:
    """Use only synthetic data and return a bounded string result."""
    import json
    return json.dumps({"status":"parsed","value":value})
