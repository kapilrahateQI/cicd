from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()


def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


def is_leap_year(year: int) -> bool:
    """Return True if the given year is a leap year, otherwise False."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


root_agent = Agent(
    name="GreetingAgent",
    model="groq/llama-3.1-8b-instant",
    description="Greets users and can perform simple calculations.",
    instruction="""
You are a helpful assistant.

You can:
- greet the user in different styles
- use the add_numbers tool to add two numbers the user provides
- use the is_leap_year tool to check whether a year is a leap year

Keep responses short and clear.
""",
    tools=[add_numbers, is_leap_year],
)