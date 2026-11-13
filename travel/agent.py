import os
from google.adk.agents import Agent
from .tools import (
    set_home_location,
    add_city,
    clear_itinerary,
    create_itinerary,
    get_destination_weather,
)

# Load prompt instructions from agent-prompt.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
instruction_file_path = os.path.join(script_dir, "instructions.txt")

with open(instruction_file_path, "r") as f:
    instruction = f.read()

model = "gemini-3.8-flash"

root_agent = Agent(
    name="travel_agent",
    description="An agent that can help plan a multi-leg journey, manage home preferences, and check weather.",
    instruction=instruction,
    model=model,
    # Register all our built tools here
    tools=[
        set_home_location,
        add_city,
        clear_itinerary,
        create_itinerary,
        get_destination_weather,
    ],
)
