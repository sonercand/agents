from google.adk import Agent


# Define standard calculator tools
def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first (a - b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divides the first number by the second (a / b). Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# Define the ADK Agent configured with your working Vertex model
root_agent = Agent(
    name="calculator",
    model="gemini-3.8-flash",  # Matches your working setup
    instruction=(
        "You are an expert mathematical assistant. "
        "Use your calculator tools to solve user equations accurately, "
        "show your working steps, and provide clear answers."
    ),
    tools=[add, subtract, multiply, divide],
)