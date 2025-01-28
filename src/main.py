from agents.graph import react_graph
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

while True:
    question = input("User: ")
    response = react_graph.invoke({"messages": HumanMessage(content=question)}, config)
    response = response['messages'][-1].content
    print("Bot: ", response)