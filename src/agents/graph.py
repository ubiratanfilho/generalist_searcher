from langgraph.graph import START, END, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from agents.assistant.agent import assistant
from agents.researcher.agent import researcher
from langgraph.checkpoint.memory import MemorySaver

# Graph
builder = StateGraph(MessagesState)

# Nodes
builder.add_node("assistant", assistant)
builder.add_node("researcher", researcher)

# Edges
builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)

# Compiling
memory = MemorySaver()
react_graph = builder.compile(checkpointer=memory)

# Saving the graph
with open("images/graph.png", "wb") as f:
    f.write(react_graph.get_graph(xray=True).draw_mermaid_png())