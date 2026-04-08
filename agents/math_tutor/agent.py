"""Math Tutor Agent using Google AI Studio (Gemini)"""

import os
from google.adk.agents import Agent
from google.genai import types

root_agent = Agent(
    name="math_tutor",
    model="gemini-2.0-flash",
    instruction="You are a friendly math tutor. Keep answers short and simple.",
)