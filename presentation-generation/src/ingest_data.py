# src/ingest_data.py
import os
from vector_db import VectorDB

def read_text_files(directory):
    texts = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            texts.append(file.read())
    return texts

if __name__ == "__main__":
    vector_db = VectorDB(config={"host": "localhost", "port": 1234})
    texts = read_text_files('data/raw_texts/')
    vector_db.insert_texts(texts)
