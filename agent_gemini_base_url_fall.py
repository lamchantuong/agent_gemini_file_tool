from langchain.agents import AgentType, initialize_agent
from langchain_openai import OpenAI
from langchain.prompts import ChatPromptTemplate
from advanced_file_tool import advanced_file_tool
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.environ.get("GEMINI_API_KEY")

# Thiết lập client cho Gemini 2.0 Flash
client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
    model="gemini-2.0-flash"
)

# Khởi tạo agent
agent = initialize_agent(
    tools=[advanced_file_tool],
    llm=client,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True
)

# prompt ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("Bạn là một nhân viên IT của công ty ABC. Bạn được yêu cầu quản lý file trong thư mục outputs (mặc định) của công ty")

result = agent.invoke({"input": "Tạo cho tôi một file mới có tên là test.txt và nội dung là 'Hello, world!'"})
print(result)







