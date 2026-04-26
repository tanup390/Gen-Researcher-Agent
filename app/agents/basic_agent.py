from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from app.tools.web_search import WebSearchTool
from app.core.memory import SimpleMemory
from app.rag.rag_engine import RAGEngine

load_dotenv()

class BasicAgent:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.web_tool = WebSearchTool()
        self.memory = SimpleMemory()
        self.rag = RAGEngine()

    def run(self, query):
        # 🧠 Memory
        history = self.memory.get_history()

        # 🌐 Web search
        web_data = self.web_tool.search(query)

        # 📚 RAG knowledge
        rag_data = self.rag.query(query)

        # 🧠 Final prompt
        prompt = f"""
        You are an advanced logistics AI agent.

        Use all available information carefully.

        Conversation History:
        {history}

        User Query:
        {query}

        Knowledge Base Data:
        {rag_data}

        Web Data:
        {web_data}

        Your job:
        - Combine all sources
        - Remove duplicate info
        - Give clear structured answer

        Output:
        - Summary
        - Key Insights
        - Latest Trends
        - Final Recommendation
        """

        response = self.llm.invoke(prompt)

        # Save memory
        self.memory.add(query, response.content)

        return response.content