from agno.agent import Agent  
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from textwrap import dedent
from agno.playground import Playground, serve_playground_app

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["AGNO_API_KEY"] = os.getenv("AGNO_API_KEY")

web_agent = Agent(
    name = "Web Agent",
    role = "Search the web for information",
    model = Groq(id = "qwen-2.5-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True,
                         company_news = True, income_statements = True)],
    instructions=dedent("""\
        You are a seasoned Wall Street analyst with deep expertise in market analysis! 📊

        Follow these steps for comprehensive financial analysis:
        1. Market Overview
           - Latest stock price
           - 52-week high and low
        2. Financial Deep Dive
           - Key metrics (P/E, Market Cap, EPS)
        3. Professional Insights
           - Analyst recommendations breakdown
           - Recent rating changes

        4. Market Context
           - Industry trends and positioning
           - Competitive analysis
           - Market sentiment indicators

        Your reporting style:
        - Begin with an executive summary
        - Use tables for data presentation
        - Include clear section headers
        - Add emoji indicators for trends (📈 📉)
        - Highlight key insights with bullet points
        - Compare metrics to industry averages
        - Include technical term explanations
        - End with a forward-looking analysis

        Risk Disclosure:
        - Always highlight potential risk factors
        - Note market uncertainties
        - Mention relevant regulatory concerns
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
)

agent_team=Agent(
    team=[web_agent,finance_agent],
    model=Groq(id="qwen-2.5-32b"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,

)
app = Playground(agents = [web_agent, finance_agent]).get_app()

if __name__== "__main__":
    serve_playground_app("multiagents:app", reload = True)

#agent_team.print_response("Analyze companies like Tesla,NVDA,Apple,Amazon and suggest which to buy for long term")