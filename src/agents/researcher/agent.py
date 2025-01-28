import dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_community.tools.tavily_search import TavilySearchResults

dotenv.load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
tools = [
    TavilySearchResults(max_results=3)
]
llm_with_tools = llm.bind_tools(tools)

# System message
sys_msg = SystemMessage(content="You are a researcher tasked with finding information on the internet.")

# Node
def researcher(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}