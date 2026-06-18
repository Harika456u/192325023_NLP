from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "Natural Language Processing is a branch of Artificial Intelligence",
    "Machine Learning is used in Artificial Intelligence",
    "Python is widely used for NLP applications",
    "Deep Learning improves language understanding"
]

# User query
query = ["Artificial Intelligence and NLP"]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Transform documents and query
tfidf_matrix = vectorizer.fit_transform(documents + query)

# Calculate similarity
similarity_scores = cosine_similarity(
    tfidf_matrix[-1], tfidf_matrix[:-1]
)

# Display ranking
print("Document Ranking:\n")

for i, score in enumerate(similarity_scores[0]):
    print(f"Document {i+1}: {score:.4f}")
