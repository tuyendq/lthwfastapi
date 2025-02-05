from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str

# Define items at application startup
items = {"apples", "oranges"}

app = FastAPI()


@app.delete("/items")
def delete_item(item: Item):
    name = item.name
    if name in items:
        items.remove(name)
    else:
        # Raise HTTPException with status code for "not found"
        raise HTTPException(status_code=404, detail="Item not found.")
    return {}


# curl -X DELETE -H 'Content-Type: application/json' -d '{"name": "bananas"}' http://localhost:8000/items

# Great work! You've created and tested your first endpoint with error handling. Now you can build endpoints that can communicate status within the application.