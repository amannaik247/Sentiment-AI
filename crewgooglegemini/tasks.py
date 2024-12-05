from crewai import Task
from tools import tool
from agents import news_researcher, news_analyzer

# Research task
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output="A comprehensive analysis of top articles in 3 paragraphs",
    tools=[tool],
    agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        "Sentiment Scoring:"
        "Analyze the sentiment of each article."
        "Provide a sentiment score between -10 and +10 based on how negative or positive the article is."
        "- A score closer to -10 indicates a more negative article."
        " - A score closer to +10 indicates a more positive article."
        "- A score of 0 indicates a neutral article."
    ),
    expected_output="Brief summary explaining each of the top articles on the given topic in bullet points and then the sentimental analysis score of each article."
    "The format should be Summary of each, then its score on new line, then overall Sentiment score of all articles, then at the end the source links of the articles",
    tools=[tool],
    agent=news_analyzer,
    async_execution=False,
    output_file="new-blog-post.md",  # Example of output customization
)
