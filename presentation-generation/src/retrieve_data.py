# src/vector_db.py (continuation)
class VectorDB:
    # existing methods

    def retrieve(self, query, top_k=5):
        return self.client.search(query, top_k)

# src/retrieve_data.py
from vector_db import VectorDB

if __name__ == "__main__":
    vector_db = VectorDB(config={"host": "localhost", "port": 1234})
    query = "example query"
    results = vector_db.retrieve(query)
    for result in results:
        print(result)
