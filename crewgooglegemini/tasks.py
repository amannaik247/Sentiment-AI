from crewai import Task
from tools import tool
from agents import news_researcher,news_analyzer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Only research top {noofarticles} articles of web page"
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends',
  tools=[tool],
  agent=news_researcher
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
  expected_output='Brief summary explaining each of the top {noofarticles} articles on the {topic} in bullet points and then the sentimental analysis score of each article',
  tools=[tool],
  agent=news_analyzer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)