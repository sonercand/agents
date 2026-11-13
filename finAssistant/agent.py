import os
from google.adk.agents import Agent
from tools import calculate_percentage_change, calculate_profit_or_loss
from search_agent import search_agent_tool

# Load instructions from agent-prompt.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
instruction_file_path = os.path.join(script_dir, "agent-prompt.txt")
with open(instruction_file_path, "r") as f:
    instruction = f.read()

model = "gemini-3.8-flash"

# Combine custom calculation tools and the search agent tool into one suite
tools = [
    calculate_percentage_change,
    calculate_profit_or_loss,
    search_agent_tool
]

# Create the root financial assistant agent
financial_assistant_agent = Agent(
    name="financial_assistant_agent",
    description="A root financial assistant that coordinates stock searching and math calculations.",
    instruction=instruction,
    model=model,
    tools=tools
)