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

### 1. Install Python

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

### 2. Why Use a Virtual Environment?

A **virtual environment** keeps your project isolated. Think of it like a separate room for each project - so packages you install for one project don't mess up other projects.

Without a venv, you might have conflicts between different projects. With a venv, each project has its own clean setup.

---

## Installation

1. **Clone the project:**
   ```bash
   git clone https://github.com/Give-a-Go/basic-agent-starter.git
   cd basic-agent-starter
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

   You should see `(venv)` appear at the start of your terminal line.

4. **Install dependencies:**
   ```bash
   pip install google-adk litellm
   ```

---

## Choose Your AI Provider

You need an API key to use an AI model. Choose one:

### Option A: Google AI Studio (Recommended for Beginners)

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key
4. Set it as an environment variable:
   ```bash
   export GOOGLE_API_KEY="your-key-here"
   ```

### Option B: Tensorix (Alternative)

1. Go to [tensorix.ai](https://tensorix.ai) and sign up
2. Get your API key from the dashboard
3. Set it as an environment variable:
   ```bash
   export TENSORIX_API_KEY="your-key-here"
   ```

> **Note:** Save your API key! You'll need to set it every time you open a new terminal. To make it permanent, add it to your shell profile (~/.zshrc or ~/.bashrc).

---

## Run the Agent

### Option 1: Terminal (CLI)

**For Google AI Studio:**
```bash
adk run agents/math_tutor
```

**For Tensorix:**
```bash
adk run agents/tensorix_math_tutor
```

Then type your math questions. Type `exit` to quit.

### Option 2: Web Browser

```bash
adk web agents
```
Then open http://127.0.0.1:8000 in your browser.

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

### The Agent Code (Simple Version)

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="math_tutor",           # Your agent's name
    model="gemini-2.0-flash",    # The AI model to use
    instruction="You are a friendly math tutor. Keep answers short and simple."
)
```

That's it! Just 5 lines to create an agent.

---

## Example Questions to Try

- What is 2 + 2?
- What is 15 * 4?
- What is the square root of 64?
- Solve x + 5 = 12

---

## Troubleshooting

**"No API key found"**
- Make sure you set the environment variable: `export GOOGLE_API_KEY="your-key"`

**"Command not found: adk"**
- Make sure you activated the venv: `source venv/bin/activate`
- Make sure you installed the packages: `pip install google-adk`

---

## Learn More

- [Google ADK Documentation](https://adk.dev/)
- [Google AI Studio](https://aistudio.google.com/)
- [Tensorix Documentation](https://docs.tensorix.ai/)