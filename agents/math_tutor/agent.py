"""Math Tutor Agent using Google AI Studio (Gemini)"""

import os
from google.adk.agents import Agent
from google.adk.callbacks import CallbackContext
from google.genai import types
from typing import Optional

def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:
    """Send a greeting on the first interaction."""
    
    session = callback_context.session
    
    # Check if this is the first message (session just started)
    if callback_context.invocation_id == 1 or not session:
        return types.Content(
            parts=[types.Part(text="Hi! I'm your friendly math tutor. Ask me any math question and I'll help you understand the answer step by step!")],
            role="model"
        )
    
    return None

root_agent = Agent(
    name="math_tutor",
    model="gemini-2.0-flash",
    instruction="You are a friendly math tutor. Keep answers short and simple.",
    before_agent_callback=before_agent_callback,
)