import os
from typing import List
from pydantic import BaseModel, Field
from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool
'''
Multi agents: web search adn structuring the output. Search and structure split into two seperate functionality
'''


script_dir = os.path.dirname(os.path.abspath(__file__))
instruction_file_path = os.path.join(script_dir, "search-prompt.txt")
with open(instruction_file_path, "r") as f:
    instruction = f.read()

model = "gemini-3.8-flash"

# Google Search Tool
tools = [google_search]

# Create an agent that uses the search tool
'''search_agent = Agent(
    name="search_agent",
    description="An agent that searches Google for stock market information.",
    instruction=instruction,
    model=model,
    tools=tools
)'''

# Define the Pydantic schema for structured stock search results
class StockSearchResult(BaseModel):
    ticker: str = Field(..., description="Stock ticker symbol")
    company_name: str = Field(..., description="Full company name")
    current_price: float = Field(..., description="Current stock price")
    change_percent: float = Field(..., description="Today's change %")
    sources: List[str] = Field(..., description="Source URLs")

# Create an agent that structures the output from the search agent using Pydantic
structured_search_agent = Agent(
    name="structured_search_agent",
    description="An agent that searches for stock information and returns structured results matching the StockSearchResult schema.",
    instruction=instruction,
    model=model,
    tools=tools,
    output_schema=StockSearchResult
)

# turn structured search agent into tool that can be called
search_agent_tool = AgentTool(agent=structured_search_agent)