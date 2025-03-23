from crewai import Agent
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv
load_dotenv()

os.environ["GOOGLE_API_KEY" ]= os.getenv("GOOGLE_API_KEY")

## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5)

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
      """You are an experienced research specialist with a talent for
        finding relevant information from various sources. You excel at
        organizing information in a clear and structured manner, making
        complex topics accessible to others"""
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    """You are a skilled News writer with expertise in
      technical writing. You have a talent for identifying patterns
      and extracting meaningful insights from research data, then
      communicating those insights effectively through well-crafted reports."""
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
