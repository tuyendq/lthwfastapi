from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

app = FastAPI()

items = {"rock", "paper", "scissors"}


@app.delete("/items")
# Make asynchronous
async def root(item: Item):
    name = item.name
    # Check if name is in items
    if name not in items:
        # Return the status code for not found
        raise HTTPException(status_code=404, detail="Item not found.")
    items.remove(name)
    return {"message": "Item deleted"}


# curl -X DELETE -H 'Content-Type: application/json' -d '{"name": "rock"}' http://localhost:8000/items
# curl -X DELETE -H 'Content-Type: application/json' -d '{"name": "roll"}' http://localhost:8000/items

# Great work! You've created and tested your first asynchronous DELETE endpoint. This is the traditional operation for endpoints that delete data managed by the API, and the final operation you need to build an application with a CRUD (Create, Read, Update & Delete) API.

