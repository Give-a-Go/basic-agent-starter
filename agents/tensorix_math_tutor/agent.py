"""Math Tutor Agent using Tensorix (OpenAI-compatible API)"""

import os
os.environ.setdefault("TENSORIX_API_KEY", "YOUR_TENSORIX_API_KEY")

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

llm = LiteLlm(
    model="openai/minimax/minimax-m2",
    api_key=os.environ.get("TENSORIX_API_KEY"),
    base_url="https://api.tensorix.ai/v1"
)

root_agent = Agent(
    name="math_tutor",
    model=llm,
    instruction="You are a friendly math tutor. When the user messages you, respond with a brief greeting like 'Hi! I'm your friendly math tutor. Ask me a math question!' Then answer their math question. Do NOT show your thoughts or reasoning. Just give the answer. Keep responses short - 1-2 sentences.",
)