# Basic Agent Starter

A simple, beginner-friendly project to get started with Google ADK (Agent Development Kit). This project creates a math tutor agent that you can run in your terminal or browser.

## What is an Agent?

An **agent** is an AI program that:
1. Takes input from a user (like a question)
2. Uses a **Model** (the AI brain) to process it
3. Follows **Instructions** (tells it how to behave)
4. Gives back a response

In this project:
- **Model**: Gemini (Google) or MiniMax (Tensorix) - the AI that generates responses
- **Instructions**: "You are a friendly math tutor" - tells the AI how to behave

## What Does This Project Do?

This is a **starter template** showing how to build a simple agent. The agent:
- Is a math tutor that answers math questions
- Can run in two ways: terminal (CLI) or web browser
- Supports two different AI providers (you can choose)

---

## Prerequisites

<details>
<summary><b>1. Install Python (click to expand)</b></summary>

**macOS:**
```bash
brew install python3
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Or use the Microsoft Store (search "Python")

**Linux:**
```bash
sudo apt install python3  # Debian/Ubuntu
sudo dnf install python3  # Fedora
```

Verify installation:
```bash
python3 --version
```
</details>

<details>
<summary><b>2. Why Use a Virtual Environment? (click to expand)</b></summary>

A **virtual environment** keeps your project isolated. Think of it like a separate room for each project - so packages you install for one project don't mess up other projects.

Without a venv, you might have conflicts between different projects. With a venv, each project has its own clean setup.
</details>

---

## Installation

1. **Clone the project:**
   ```bash
   git clone https://github.com/Give-a-Go/basic-agent-starter.git
   ```

2. **Go into the project folder:**
   ```bash
   cd basic-agent-starter
   ```

3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**

   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   You should see `(venv)` appear at the start of your terminal line.

5. **Install dependencies:**

   **If using Google AI Studio only:**
   ```bash
   pip install google-adk
   ```

   **If using Tensorix (or both):**
   ```bash
   pip install "google-adk[extensions]"
   ```

   > If you get a permission error, add `--break-system-packages`: `pip install --break-system-packages "google-adk[extensions]"`

   > Make sure your virtual environment is activated (you should see `(venv)` in your terminal).

---

## Choose Your AI Provider

You need an API key to use an AI model.

> **Important:** Both options work! Tensorix has more free credits. If you have issues with one, try the other.

### Option A: Tensorix (More Free Credits)

Tensorix offers more free credits and works well for this project.

1. Go to [tensorix.ai](https://tensorix.ai) and sign up
2. Get your API key from the dashboard
3. Set it as an environment variable:
   ```bash
   export TENSORIX_API_KEY="your-key-here"
   ```

4. **Run with Tensorix:**
   ```bash
   adk run agents/tensorix_math_tutor
   ```

### Option B: Google AI Studio

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key
4. Set it as an environment variable:
   ```bash
   export GOOGLE_API_KEY="your-key-here"
   ```

5. **Run with Google AI Studio:**
   ```bash
   adk run agents/math_tutor
   ```

> **Note:** Save your API key! You'll need to set it every time you open a new terminal. To make it permanent, add it to your shell profile (~/.zshrc or ~/.bashrc).

---

## Run the Agent

### Option 1: Web Browser (Recommended)

The easiest way to use your agent - opens in your browser with a nice chat interface.

```bash
adk web agents
```
Then open http://127.0.0.1:8000 in your browser.

### Option 2: Terminal (CLI) - Alternative

If you prefer the command line:

**For Tensorix (More Free Credits):**
```bash
adk run agents/tensorix_math_tutor
```

**For Google AI Studio:**
```bash
adk run agents/math_tutor
```

Then type your math questions. Type `exit` to quit.

---

## How It Works

### Project Structure

```
basic-agent-starter/
├── agents/
│   ├── math_tutor/              # Uses Google AI Studio
│   │   ├── __init__.py          # Makes this a Python package
│   │   └── agent.py             # The agent definition
│   └── tensorix_math_tutor/     # Uses Tensorix
│       ├── __init__.py
│       └── agent.py
├── .gitignore
└── README.md
```

### The Agent Code (Tensorix Version)

```python
import os
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
    instruction="You are a friendly math tutor. Keep answers short and simple."
)
```

### The Agent Code (Google AI Studio Version)

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="math_tutor",
    model="gemini-2.0-flash",
    instruction="You are a friendly math tutor. Keep answers short and simple."
)
```

---

## Example Questions to Try

- What is 2 + 2?
- What is 15 * 4?
- What is the square root of 64?
- Solve x + 5 = 12

---

## Troubleshooting

**"No API key found"**
- Make sure you set the environment variable: `export GOOGLE_API_KEY="your-key"` or `export TENSORIX_API_KEY="your-key"`

**"Command not found: adk"**
- Make sure you activated the venv: `source venv/bin/activate`
- Make sure you installed the packages: `pip install google-adk`

**"Fail to load 'tensorix_math_tutor.agent' module. LiteLLM support requires..."**
- Install with extensions (note the quotes around the brackets):
  ```bash
  pip install "google-adk[extensions]"
  ```
- If you get a permission error, use: `pip install --break-system-packages "google-adk[extensions]"`
- Make sure you're in your virtual environment (you should see `(venv)` in your terminal)

**"cannot import name 'LiteLLM' from 'google.adk.models'"**
- Your version of google-adk is older and doesn't support LiteLLM
- **Solution:** Use Google AI Studio instead (simpler!)
- Run: `adk run agents/math_tutor` (after setting `GOOGLE_API_KEY`)

**"RESOURCE_EXHAUSTED" or "You exceeded your current quota"**
- You've hit the free tier limit on Google AI Studio
- **Solution:** Switch to Tensorix instead (more free credits)
- Run: `adk run agents/tensorix_math_tutor` (after setting TENSORIX_API_KEY)

**"AttributeError: module aiohttp has no attribute ClientConnectorDNSError"**
- This is a version compatibility issue
- **Solution:** Upgrade aiohttp:
  ```bash
  pip install --upgrade aiohttp
  ```

**"module 'aiohttp' has no attribute 'ClientConnectorError'"**
- Same compatibility issue
- **Solution:** Upgrade packages:
  ```bash
  pip install --upgrade google-adk aiohttp
  ```

---

## Learn More

- [Google ADK Documentation](https://adk.dev/)
- [Google AI Studio](https://aistudio.google.com/)
- [Tensorix Documentation](https://docs.tensorix.ai/)