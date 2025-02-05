from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

app = FastAPI()


@app.post("/")
def root(item: Item):
    name = item.name
    return {"message": f"We have {name}"}

# Great work! You've created and tested your first POST endpoint. Now you can build endpoints that traditionally create new objects and can functionally accept virtually limitless input data.