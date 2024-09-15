from crewai import Task
from tools import tool
from agents import news_researcher,news_analyzer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Your final report should clearly articulate the key points,"
    "its market opportunities, and potential risks."
  ),
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=news_researcher
)

# Writing task with language model configuration
write_task = Task(
  description=(
    "Sentiment Scoring:"
    "Analyze the sentiment of the news article."
    "Provide a sentiment score between -10 and +10 based on how negative or positive the article is."
      "- A score closer to -10 indicates a more negative article."
      " - A score closer to +10 indicates a more positive article."
      "- A score of 0 indicates a neutral article."
      
     "Net Impact Analysis"
      "Assess the overall impact of the trends or developments described in the article on the industry or the relevant field."
      "Mention whether the impact seems positive, negative, or neutral."

  "Summary:"
   "- Write a brief, engaging summary in bullet points of the main points discussed in the article."
   "- Focus on highlighting key trends, developments, and any important information that impacts the industry."
   "- The summary should be easy to understand and concise."
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_analyzer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)