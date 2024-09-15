from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define your function here
def your_function(input: str, no_of_articles: int):
    # Your function logic goes here
    return {"input_received": input, "no_of_articles_received": no_of_articles}

# Define the request body model
class ArticleRequest(BaseModel):
    input: str
    no_of_articles: int

# Create the endpoint
@app.post("/process_input/")
async def process_input(request: ArticleRequest):
    result = your_function(request.input, request.no_of_articles)
    return result
