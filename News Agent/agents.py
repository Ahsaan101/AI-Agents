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
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
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
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
