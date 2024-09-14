from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
#call the gemini models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature =0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY")
                             )

# Creating a senior researcher agent with memory and verbose mode

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
    
)

## Creating a writer agent with custom tools responsible in writing new blog

news_writer = Agent(
    role="Writer",
    goal="Craft compelling content on {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging content that captivates and educates, bringing new ideas"
        "to life in a concise and informative manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False

)
