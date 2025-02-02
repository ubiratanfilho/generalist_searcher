from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_community.tools import TavilySearchResults

from pydantic import BaseModel, Field

class NeedWebSearch(BaseModel):
    """Boolean flag to indicate if web search is needed"""
    
    web_search: bool = Field(description="Boolean flag to indicate if web search is needed")

def search_web(state):
    """ Retrieve docs from web search """
    
    print("---SEARCH WEB---")
    
    # Search
    tavily_search = TavilySearchResults(max_results=10)
    search_docs = tavily_search.invoke(state['question'])

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
    
    print("---ASSISTANT---")
    
    llm = ChatOpenAI(model="gpt-4o-mini")
    
    # Get state
    context = state["context"]
    messages = state["messages"]
    web_search = state["web_search"]
    
    # Web search check chain
    if not web_search:
        web_search_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a grader assessing if you need to search the web for more information."
                    "To do so, think if you can answer the user with what you know. If you can't, you must output 'True'."
                    "Otherwise, output 'False'."
                ),
                MessagesPlaceholder(variable_name="messages")
            ]
        )
        web_search_chain = web_search_template | llm.with_structured_output(NeedWebSearch)
        web_search = web_search_chain.invoke({"messages": messages}).web_search
        if web_search:
            print("---WEB SEARCH NEEDED---")
            return {"web_search": web_search}

    # Answer chain
    answer_template = ChatPromptTemplate.from_messages(
        [
            (
                "system", 
                "You are a helpful assistant that can answer questions about anything except Civil Engineering."
                "Use the context of the following documents to answer the user's question: '{context}'"
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    chain = answer_template | llm
    answer = chain.invoke({"messages": messages, "context": context})
    
    # Append it to state
    return {"messages": [answer], "web_search": False}