"""
FastAPI REST API Starter Code

This is a starter template for building a REST API with FastAPI.
Complete the TODO sections to implement the assignment requirements.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI(
    title="My REST API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)

# TODO: Define a Pydantic model for request data
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# TODO: Implement a GET endpoint that returns a welcome message
@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Welcome to my FastAPI application"}


# TODO: Implement a GET endpoint that returns a list of items
@app.get("/items")
def get_items():
    """Endpoint that returns a list of sample items."""
    return {"items": []}


# TODO: Implement a POST endpoint that accepts an Item and returns it
@app.post("/items")
def create_item(item: Item):
    """Endpoint that creates a new item with validation."""
    return {"item": item}


# Run the application with: uvicorn starter-code:app --reload
# Then visit http://localhost:8000/docs to see the interactive API documentation
