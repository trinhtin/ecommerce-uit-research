from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import JSONLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")


logging.info("Loading Json")
loader = JSONLoader(
    file_path=r"../../Data/luat-an-ninh-quoc-gia.json",
    jq_schema=".noi_dung[].chuong.ten",
    text_content=False,
)

documents = loader.load()

logging.info("Loading embedding models")
embedding_function = OpenAIEmbeddings()

logging.info(
    "Instantiate a Chroma DB instance from the documents & the embedding model"
)
db = Chroma.from_documents(documents, embedding_function)
retriever = db.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI()
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

query = "Nội dung của dữ liệu là gì"
print(chain.invoke(query))
