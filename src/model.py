from langchain.llms import OpenAI
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent
)
from chroma.vector_database import chroma_vectordb
from dotenv import load_dotenv
import os

load_dotenv()


os.environ['OPENAI_API_KEY'] = os.environ['open_ai_api']
api_key = os.getenv('API_KEY')

def create_model_and_agent():
    toolkit, _ = chroma_vectordb()
    # Create instance of OpenAI LLM
    llm = OpenAI(temperature=0.1,verbose=False, api_key=api_key)
    # Add the toolkit to an end-to-end LC
    agent_executor = create_vectorstore_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )
    return agent_executor