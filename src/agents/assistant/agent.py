import dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

dotenv.load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

# System message
sys_msg = SystemMessage(content="You are a helpful assistant that can talk about every topic, besides Civil Engineering.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm.invoke([sys_msg] + state["messages"])]}