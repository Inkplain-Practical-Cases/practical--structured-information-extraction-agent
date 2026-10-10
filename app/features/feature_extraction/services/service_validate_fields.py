# Validation service: enforce expected types and a valid ISO date, if provided.
from datetime import date
from pydantic import BaseModel, EmailStr, ValidationError, field_validator
class ExtractedRecord(BaseModel):
    customer_email: str | None
    request_category: str
    requested_date: str | None
    @field_validator("requested_date")
    @classmethod
    def check_date(cls,v):
        if v is not None: date.fromisoformat(v)
        return v

def validate_fields(data:dict)->dict:
    return ExtractedRecord.model_validate(data).model_dump()
