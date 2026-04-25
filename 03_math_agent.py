# 03_math_agent.py
# LangChain math agent using custom math tools
# Concept: Agent that can perform math operations using custom tools

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

# Load API key from .env
load_dotenv()

# 1. Custom math tools


@tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a-b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a*b


@tool
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        return "ERROR: Cannot Divide by zero!"
    return a/b


# 2. LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 3. Give tools to agent
tools = [add, subtract, multiply, divide]
agent = create_agent(llm, tools=tools)

# 4. Run - ask a math question
response = agent.invoke({
    "messages": [("human", "What is 25 multiplied by 4, then divided by 2, then subtract 10?")]
})

print("\nFinal Answer:", response["messages"][-1].content)
