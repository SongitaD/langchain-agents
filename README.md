# LangChain Agents

A collection of Python programs exploring LangChain agents — built step by step while learning AI/ML development.

## Programs

| File | Concept | Description |
|------|---------|-------------|
| 01_basic_agent.py | AgentExecutor | Basic agent that searches Wikipedia |
| 02_custom_tools.py | Custom Tools | Agent with custom weather and population tools |
| 03_math_agent.py | Math Tool | Coming soon |
| 04_search_agent.py | Search Tool | Coming soon |
| 05_multi_tool_agent.py | Multiple Tools | Coming soon |

## Concepts Covered

- LangChain agents vs raw OpenAI API
- Built-in tools (Wikipedia, DuckDuckGo)
- Custom tools
- AgentExecutor loop

## Setup

```bash
git clone https://github.com/yourusername/langchain-agents.git
cd langchain-agents
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install langchain langchain-openai langchain-community wikipedia python-dotenv
```

## Environment Variables

Create a `.env` file in the root folder:
OPENAI_API_KEY=your_key_here
