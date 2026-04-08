"""Math Tutor Agent using Google AI Studio (Gemini)"""

import os
from google.adk.agents import Agent

root_agent = Agent(
    name="math_tutor",
    model="gemini-2.0-flash",
    instruction="You are a friendly math tutor. Always greet the user warmly when you first respond, then help with math. Keep answers short and simple.",
)