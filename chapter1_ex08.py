# Import date
from datetime import date

# Import BaseModel
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str
    quantity: int = 0
    expiration: date = None

# Great work! You've created and tested your first Pydantic model. Now you can build endpoints that accept your model as input and/or return your model as output.