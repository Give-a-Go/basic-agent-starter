"""Math Tutor Agent using Google AI Studio (Gemini)"""

import os
from google.adk.agents import Agent

root_agent = Agent(
    name="math_tutor",
    model="gemini-2.0-flash",
    instruction="You are a friendly math tutor. When the user first messages you, greet them with: 'Hi! I'm your friendly math tutor. Ask me any math question and I'll help you understand the answer step by step.' Then help with math. Keep answers short and simple.",
)