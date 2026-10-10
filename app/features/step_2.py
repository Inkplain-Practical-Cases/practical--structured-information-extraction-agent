"""STEP-2 deterministic feature: Call offline extraction provider.
ICS layer: service.
Why it exists: lets readers isolate the capability from the API door.
Without it: the associated business transformation would not execute.
"""
def transform(value:str)->str:
    """Use only synthetic data and return a bounded string result."""
    import json
    return json.dumps({"intent":"help" if "help" in value.lower() else "other","length":len(value)})
