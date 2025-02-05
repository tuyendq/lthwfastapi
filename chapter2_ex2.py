from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str
    description: str

# Define items at application start
items = {"bananas": "Yellow fruit."}

app = FastAPI()


@app.put("/items")
def update_item(item: Item):
    name = item.name
    # Update the description
    items[name] = item.description
    return item
    
 
 
# curl -X PUT -H 'Content-Type: application/json' -d '{"name":"bananas", "description":"Delicious!"}' http://localhost:8000/items
# {"name":"bananas","description":"Delicious!"}


# Great work! You've created and tested your first PUT endpoint. Now you can build endpoints that traditionally update existing objects.
