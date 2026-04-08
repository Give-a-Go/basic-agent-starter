# Math Tutor Agent

A simple math tutor agent built with Google ADK (Agent Development Kit). This project provides two options for the LLM backend:
- **Google AI Studio** (Gemini models) - default
- **Tensorix** (MiniMax models) - alternative

## Prerequisites

1. **Python 3.10+** installed
2. **Clone or download** this project

---

## Installation

1. Navigate to the project folder:
   ```bash
   cd my-agent
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install google-adk litellm
   ```

---

## Option 1: Google AI Studio (Gemini)

Uses Google's Gemini models. You need a Google AI Studio API key.

### Get API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create an API key
3. Set the environment variable (or add to your shell profile):
   ```bash
   export GOOGLE_API_KEY="your-google-api-key"
   ```

### Run the Agent

**Using ADK CLI (Terminal):**
```bash
adk run agents/math_tutor
```

**Using ADK Web Interface:**
```bash
adk web agents
```
Then open http://127.0.0.1:8000 in your browser.

---

## Option 2: Tensorix (MiniMax)

Uses Tensorix's OpenAI-compatible API with MiniMax models. You need a Tensorix API key.

### Get API Key
1. Sign up at [tensorix.ai](https://tensorix.ai)
2. Get your API key from the dashboard
3. Set the environment variable:
   ```bash
   export TENSORIX_API_KEY="your-tensorix-api-key"
   ```

### Run the Agent

**Using ADK CLI (Terminal):**
```bash
adk run agents/tensorix_math_tutor
```

**Using ADK Web Interface:**
```bash
adk web agents
```
Then open http://127.0.0.1:8000 in your browser.

---

## Project Structure

```
my-agent/
├── agents/
│   ├── math_tutor/           # Google AI Studio version
│   │   ├── __init__.py
│   │   └── agent.py
│   └── tensorix_math_tutor/   # Tensorix version
│       ├── __init__.py
│       └── agent.py
├── venv/                     # Virtual environment (created after setup)
└── README.md
```

---

## Usage

After starting the agent, type your math questions. Type `exit` to quit (CLI mode only).

Example questions:
- What is 2 + 2?
- What is 15 * 4?
- Solve x + 5 = 12

---

## Learn More

- [Google ADK Documentation](https://adk.dev/)
- [Tensorix Documentation](https://docs.tensorix.ai/)
- [Google AI Studio](https://aistudio.google.com/)