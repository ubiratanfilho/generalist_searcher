from langgraph.graph import START, END, StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver

from langchain_core.messages import BaseMessage

from typing import List

from utils.nodes import *

# States
class State(MessagesState):
    question: str
    context: List[str]
    web_search: bool

# Graph
builder = StateGraph(State)

builder.add_node("search_web", search_web)
builder.add_node("assistant", assistant)

builder.add_edge(START, "assistant")

def conditional_search(state: List[BaseMessage]) -> str:
    if state["web_search"]:
        return "search_web"
    return END

builder.add_conditional_edges("assistant", conditional_search)
builder.add_edge("search_web", "assistant")

graph = builder.compile(checkpointer=MemorySaver())

# with open("images/graph.png", "wb") as f:
#     f.write(graph.get_graph(xray=True).draw_mermaid_png())