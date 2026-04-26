from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

class WebSearchTool:
    def __init__(self):
        self.client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def search(self, query):
        response = self.client.search(query=query, search_depth="basic")
        
        results = []
        for r in response["results"]:
            results.append(r["content"])
        
        return "\n".join(results)