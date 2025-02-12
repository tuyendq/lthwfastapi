from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# define model Quote
class Quote(BaseModel):
    text: str
    author: str

app = FastAPI()

quotes = []

@app.post("/quotes")
def create(quote: Quote):
    text = quote.text
    author = quote.author
    for quote in quotes:
        if text in quote['text']:
            raise HTTPException(status_code=409, detail="Quote exists")
    # if text in quotes:
    #     raise HTTPException(status_code=409, detail="Quote exists")
    quotes.append({"text":text, "author": author})
    return {"message": f"Added '{text}' to quotes."}

@app.get("/")
def read_quotes():
    """Return all quotes."""
    # return quotes
    return JSONResponse(content=quotes)

# @app.get("/items")
# def read(name: str):
#     if name not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return items[name]  
  
# @app.put("/items")
# def update(item: Item):
#     name = item.name
#     if name not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     items[name] = item
#     return {"message": f"Updated {name}."}
  
@app.delete("/quotes")
def delete(quote: Quote):
    text = quote.text
    for quote in quotes:
        if text in quote['text']:
            quotes.remove(quote)
            return {"message": f"Deleted '{text}'."}
    raise HTTPException(status_code=404, detail="Quote not found")