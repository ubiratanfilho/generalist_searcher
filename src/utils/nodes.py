import dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.types import Command
from langchain_core.messages import SystemMessage, HumanMessage
from typing_extensions import Literal
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from utils.tools import *

dotenv.load_dotenv()

def search_web(state):
    
    """ Retrieve docs from web search """

    # Search
    tavily_search = TavilySearchResults(max_results=3)
    search_docs = tavily_search.invoke(state['messages'][-1].content)

    # Format
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document href="{doc["url"]}"/>\n{doc["content"]}\n</Document>'
            for doc in search_docs
        ]
    )

    return {"context": [formatted_search_docs]} 

def assistant(state):
    
    """ Node to answer a question """

    llm = ChatOpenAI(model="gpt-4o-mini")
    
    # Get state
    context = state["context"]
    messages = state["messages"]

    # Template
    answer_template = ChatPromptTemplate.from_messages(
        [
            (
                "system", 
                "You are a helpful assistant that can answer questions about anything except Civil Engineering."
                "Use the context of the following documents to answer the user: '{context}'"
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    chain = answer_template | llm
    # Answer
    answer = chain.invoke({"messages": messages, "context": context})
    
    # Append it to state
    return {"messages": [answer]}