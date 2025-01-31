import dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

dotenv.load_dotenv()

# tool for web search
web_search = TavilySearchResults(max_results=10)