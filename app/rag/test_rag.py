from app.rag.rag_engine import RAGEngine

rag = RAGEngine()

query = "What is logistics?"

result = rag.query(query)

print("\nRAG Result:\n")
print(result)