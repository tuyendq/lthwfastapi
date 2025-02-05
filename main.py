from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define model Quote
class Quote(BaseModel):
    quote: str
    author: str

app = FastAPI()

quotes = {}

@app.get("/")
def read_root():
    # return {"Hello": "World"}
    return {}
