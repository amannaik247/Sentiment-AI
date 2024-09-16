from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
# from langchain_google_genai import ChatGoogleGenerativeAI
import os


"""
#call the gemini models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature =0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY")
                             )
"""

## load the Groq API key
groq_api_key=os.environ["GROQ_API_KEY"]
# call groq models
llm=ChatGroq(groq_api_key=groq_api_key,
             temperature =0.5,
             model_name="groq/llama-3.1-70b-versatile")


# Creating a senior researcher agent with memory and verbose mode

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground breaking news about {topic}",
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

news_analyzer = Agent(
    role="Writer",
    goal="Craft compelling content on {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for analyzing complex topics, you analyze the current"
        "state of the art in the industry and give accurate sentimental analysis"
        "on the topic."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False

)
