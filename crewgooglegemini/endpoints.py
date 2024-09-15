from fastapi import FastAPI
from pydantic import BaseModel
from crewai import Crew,Process
from tasks import research_task, write_task
from agents import news_researcher,news_analyzer

## Forming the tech focused crew with some enhanced configuration
app = FastAPI()

# Define your function here
def your_function(topic: str, noofarticles: int):
    crew=Crew(
    agents=[news_researcher,news_analyzer],
    tasks=[research_task,write_task],
    process=Process.sequential
)
    result=crew.kickoff(inputs={'topic': topic, 'noofarticles': noofarticles})
    print(result)
    with open("new-blog-post.txt", 'r') as file:
        content = file.read()
    return content

# Define the request body model
class ArticleRequest(BaseModel):
    topic: str
    noofarticles: int

# Create the endpoint
@app.post("/process_input/")
async def process_input(request: ArticleRequest):
    result = your_function(request.topic, request.noofarticles)
    return result
