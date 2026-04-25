# 02_custom_tools.py
# Langchain custom tools
# Concept: Build your own tools and give them to the agent

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

# Load API key from .env
load_dotenv()

# 1. Define custom tools using @tool


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # Fake data - no API key needed
    weather_data = {
        "london": "Cloudy, 15°C",
        "new york": "Sunny, 22°C",
        "tokyo": "Rainy, 18°C",
        "sydney": "Sunny, 28°C",
        "paris": "Partly cloudy, 17°C"
    }
    return weather_data.get(city.lower(), f"Weather data not available for {city}")


@tool
def get_population(city: str) -> str:
    """Get the population of a given city."""
    population_data = {
        "london": "9.5 million",
        "new york": "8.3 million",
        "tokyo": "13.9 million",
        "sydney": "5.3 million",
        "paris": "2.1 million"
    }
    return population_data.get(city.lower(), f"Population data not available for {city}")


# 2. LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 3. Give tools to agent
tools = [get_weather, get_population]
agent = create_agent(llm, tools=tools)

# 4. Run - agent will decide which tool to use
response = agent.invoke({
    "messages": [("human", "What is the weather and population of Tokyo?")]
})

print("\nFinal Answer:", response["messages"][-1].content)
