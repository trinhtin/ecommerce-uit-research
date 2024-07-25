# src/generate_responses.py
from vector_db import VectorDB
from llm import LLM

if __name__ == "__main__":
    vector_db = VectorDB(config={"host": "localhost", "port": 1234})
    llm = LLM(config={"api_key": "your_api_key"})

    query = "example query"
    retrieved_texts = vector_db.retrieve(query)

    context = " ".join(retrieved_texts)
    response = llm.generate_response(context)
    print(response)