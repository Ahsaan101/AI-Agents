from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
  """Conduct an in-depth analysis to identify the emerging trends in {topic}.
    Emphasize the advantages, disadvantages, and the overarching narrative.
    The final report should clearly present the key insights,market opportunities, and potential risks."""
  ),
  
  expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
  tools=[tool],
  agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
  description=(
    """Craft an engaging and informative article on {topic}.
      Highlight the latest trends and their impact on the industry.
      The article should be clear, engaging, and maintain a positive tone."""
  ),
  expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Example of output customization
)