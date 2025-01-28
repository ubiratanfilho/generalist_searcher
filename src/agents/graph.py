from langgraph.graph import START, END, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from agents.assistant.agent import assistant
from agents.researcher.agent import researcher

# Graph
builder = StateGraph(MessagesState)

# Define nodes: these do the work
builder.add_node("assistant", assistant)
builder.add_node("researcher", researcher)

# Define edges: these determine how the control flow moves
builder.add_edge(START, "assistant")
builder.add_edge("assistant", END)
react_graph = builder.compile()

# show the graph
with open("images/graph.png", "wb") as f:
    f.write(react_graph.get_graph(xray=True).draw_mermaid_png())