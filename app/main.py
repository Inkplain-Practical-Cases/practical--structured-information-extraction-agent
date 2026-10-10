# FastAPI door delegates request handling to a separate feature handler.
from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.features.feature_extraction.handlers.handle_extract import handle_extract
app=FastAPI(title="Structured Information Extraction Agent")
class Request(BaseModel):
    message: str = Field(min_length=1,max_length=2000)
@app.post("/process")
def process(request:Request)->dict:
    return handle_extract(request.message)
