from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableConfig, chain

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