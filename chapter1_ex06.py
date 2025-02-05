from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

# Define a route at the root web address ("/")
@app.get("/")
async def root(name: str="Alan"):
    return {"message": f"Hello {name}"}
