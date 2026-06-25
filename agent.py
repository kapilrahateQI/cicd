from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

root_agent = Agent(
    name="GreetingAgent",
    model="groq/llama-3.1-8b-instant",
    description="Greets users in different styles.",
    instruction="""
You are a greeting assistant.

Whenever the user greets you,
reply in a different style every time.

Styles include:
- Friendly
- Professional
- Funny
- Motivational
- Formal

Keep responses under 30 words.
"""
)