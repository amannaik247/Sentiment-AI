import streamlit as st
from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_analyzer


# Streamlit input fields
st.title("Sentiment AI")

# Get user input for topic and number of articles
topic = st.text_input("Enter the topic")
noofarticles = st.number_input(
    "Enter the number of articles", min_value=4, step=1, max_value=10
)
if st.button("Start Web Analysis"):
    # Forming the tech-focused crew with enhanced configuration
    crew = Crew(
        agents=[news_researcher, news_analyzer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )

    # Starting the task execution process with enhanced feedback
    result = crew.kickoff(inputs={"topic": topic, "noofarticles": str(noofarticles)})
    with open("new-blog-post.md", "r") as file:
        content = file.read()
    st.write(content)
