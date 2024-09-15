from crewai import Crew,Process
from tasks import research_task, write_task
from agents import news_researcher,news_analyzer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_analyzer],
    tasks=[research_task,write_task],
    process=Process.sequential
)

## starting the task execution process wiht enhanced feedback
result=crew.kickoff(inputs={'topic':'Polycab India', 'noofarticles':'4'})
print(result)