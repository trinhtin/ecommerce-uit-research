from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI

load_dotenv()

path = r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\luat-an-ninh-quoc-gia.txt"

documents = TextLoader(path, autodetect_encoding=True).load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=20, length_function=len
)

all_splits = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    return_source_documents=True,
)

question = "Nội dung của dữ liệu là gì"
result = qa({"query": question})

print(result)
