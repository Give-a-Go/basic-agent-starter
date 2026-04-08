"""Math Tutor Agent using Tensorix (OpenAI-compatible API)"""

import os
os.environ.setdefault("TENSORIX_API_KEY", "YOUR_TENSORIX_API_KEY")

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.callback_context import CallbackContext
from google.genai import types
from typing import Optional

def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """Send greeting on first interaction."""
    session = callback_context.session
    if session:
        events = session.events if hasattr(session, 'events') else []
        if not events or len(events) == 0:
            return types.Content(
                parts=[types.Part(text="Hi! I'm your friendly math tutor. Ask me any math question and I'll help you understand the answer step by step!")],
                role="model"
            )
    return None

llm = LiteLlm(
    model="openai/minimax/minimax-m2",
    api_key=os.environ.get("TENSORIX_API_KEY"),
    base_url="https://api.tensorix.ai/v1"
)

root_agent = Agent(
    name="math_tutor",
    model=llm,
    instruction="You are a friendly math tutor. Keep answers short and simple.",
    before_agent_callback=before_agent_callback,
)