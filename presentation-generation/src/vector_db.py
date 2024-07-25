# src/vector_db.py
from sentence_transformers import SentenceTransformer
import faiss

class VectorDB:
    def __init__(self, config):
        self.client = VectorDBClient(config)

    def insert_texts(self, texts):
        for text in texts:
            self.client.insert(text)
            
    
    
from sentence_transformers import SentenceTransformer

# Load pre-trained Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example text data
texts = [
    "This is the first sentence.",
    "Here is another sentence.",
    "FAISS is great for similarity search.",
    "We are converting text to vectors."
]

# Convert texts to vectors
vectors = model.encode(texts)


import faiss

# Dimensions of the vectors (depends on the embedding model used)
d = vectors.shape[1]

# Create a FAISS index
index = faiss.IndexFlatL2(d)

# Add vectors to the index
index.add(vectors)

# Optional: Save the index to disk
faiss.write_index(index, 'faiss_index.bin')

            
            
            