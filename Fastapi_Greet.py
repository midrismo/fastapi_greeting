from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI(
    title="My First API",
    description="A basic beginner API built with FastAPI"
)

# Root endpoint (GET /)
@app.get("/")
def read_root():
    return {"message": "Welcome to my basic FastAPI application!"}

# Path parameter endpoint (GET /greet/{name})
@app.get("/greet/{name}")
def greet_person(name: str):
    return {
        "greeting": f"Hello, {name}!",
        "note": "This name was passed through the URL path."
    }

# Query parameter endpoint (GET /search?q=something) - Bonus
@app.get("/search")
def search_item(q: str = "No search term provided"):
    return {
        "search_query": q,
        "message": "This value was passed as a query parameter."
    }