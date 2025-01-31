from langgraph.graph import START, END, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.checkpoint.memory import MemorySaver

from typing import Annotated

import operator

from typing_extensions import TypedDict

from utils.nodes import *
from utils.tools import *

# States
class State(TypedDict):
    question: str
    answer: str
    context: Annotated[list, operator.add]
    
# Graph
builder = StateGraph(State)

builder.add_node("search_web", search_web)
builder.add_node("generate_answer", generate_answer)

builder.add_edge(START, "search_web")
builder.add_edge("search_web", "generate_answer")
builder.add_edge("generate_answer", END)

graph = builder.compile(checkpointer=MemorySaver())

with open("images/graph.png", "wb") as f:
    f.write(graph.get_graph(xray=True).draw_mermaid_png())