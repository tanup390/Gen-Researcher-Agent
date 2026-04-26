from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",   # ✅ updated model
    api_key=os.getenv("GROQ_API_KEY")
)

# Test query
response = llm.invoke("Explain logistics industry in simple terms")

print("\nAI Response:\n")
print(response.content)