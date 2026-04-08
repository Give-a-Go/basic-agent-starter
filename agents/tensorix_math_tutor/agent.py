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
    instruction="You are a friendly math tutor. Always greet the user warmly when you first respond, then help with math. Keep answers short and simple.",
)