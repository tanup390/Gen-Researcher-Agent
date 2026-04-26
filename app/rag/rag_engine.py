from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RAGEngine:
    def __init__(self):
        self.documents = []
        self.vectorizer = TfidfVectorizer()

    def add_document(self, doc, doc_id):
        self.documents.append(doc)

    def query(self, query):
        if not self.documents:
            return "No data available"

        vectors = self.vectorizer.fit_transform(self.documents + [query])
        
        similarity = cosine_similarity(vectors[-1], vectors[:-1])
        
        best_match_index = similarity.argmax()
        
        return self.documents[best_match_index]