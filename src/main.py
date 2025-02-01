from utils.graph import graph
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

while True:
    question = input("User: ")
    response = graph.invoke({"question": question}, config)
    response = response['answer'].content
    print("Bot: ", response)