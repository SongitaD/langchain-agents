# 01_basic_agent.py
# LangChain basic agent using OpenAI and a built-in tool
# Concept: How LangChain's AgentExecutor automates the agent loop

# 01_basic_agent.py
# LangChain basic agent using OpenAI and Wikipedia tool
# Concept: Agent automatically decides when to use tools

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Load API key from .env
load_dotenv()

# 1. LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 2. Tool - Wikipedia (free, no API key needed)
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
tools = [wiki]

# 3. Create agent (modern way)
agent = create_agent(llm, tools=tools)

# 4. Run
response = agent.invoke(
    {"messages": [("human", "What is LangChain and who created it?")]})
print("\nFinal Answer:", response["messages"][-1].content)
