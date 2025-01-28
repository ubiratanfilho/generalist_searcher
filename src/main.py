from agents.graph import react_graph
from langchain_core.messages import HumanMessage

while True:
    question = input("User: ")
    response = react_graph.invoke({"messages": HumanMessage(content=question)})
    response = response['messages'][-1].content
    print("Bot: ", response)