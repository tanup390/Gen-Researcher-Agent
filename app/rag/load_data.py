from app.rag.rag_engine import RAGEngine

rag = RAGEngine()

docs = [
    "Logistics includes transportation, warehousing, and supply chain management.",
    "AI improves logistics through automation and demand prediction.",
    "Last mile delivery is the most expensive and complex part of logistics.",
    "Green logistics focuses on reducing carbon emissions.",
]

for i, doc in enumerate(docs):
    rag.add_document(doc, str(i))

print("✅ Data loaded into RAG system")