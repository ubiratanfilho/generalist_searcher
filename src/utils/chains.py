from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

# Assistant Chain
assistant_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that can answer questions about anything except Civil Engineering."
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)
assistant_chain = assistant_template | llm

# Researcher Chain
researcher_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a researcher that can search for information on the web."
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)
researcher_chain = researcher_template | llm

if __name__ == "__main__":
    while True:
        question = input("User: ")
        response = assistant_chain.invoke({"messages": [question]})
        print("Bot: ", response)