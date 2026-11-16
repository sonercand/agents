import os
from google.adk.agents import Agent
from google.adk.tools.toolbox_toolset import ToolboxToolset

# Load instructions from agent-prompt.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
instruction_file_path = os.path.join(script_dir, "agent-prompt.txt")
with open(instruction_file_path, "r") as f:
    instruction = f.read()

# Connect to the MCP Toolbox server running on port 5001
toolbox_url = os.getenv("TOOLBOX_URL", "http://127.0.0.1:5001")
toolset = ToolboxToolset(server_url=toolbox_url)

# Configure the ADK root agent
root_agent = Agent(
    name="warehouse_manager_agent",
    description="A warehouse inventory manager that handles stock operations and enforces audit logging via SQL tools.",
    instruction=instruction,
    model="gemini-3.8-flash",
    tools=[toolset],
)