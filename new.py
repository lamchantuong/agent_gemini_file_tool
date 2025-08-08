from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import Tool
from langchain_community.utilities import GoogleSearchAPIWrapper

from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.environ.get("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=gemini_api_key,
    temperature=0.0,
)

response = llm.invoke("What is the capital of France?")

print(response)






