from chromadb import PersistentClient
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from langchain_community.document_loaders import JSONLoader
import os
import openai
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

if os.getenv("OPENAI_API_KEY") is not None:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("OPENAI_API_KEY is ready")
else:
    print("OPENAI_API_KEY environment variable not found")

EMBEDDING_MODEL = "text-embedding-3-small"
embedding_function = OpenAIEmbeddingFunction(
    api_key=os.environ.get("OPENAI_API_KEY"), model_name=EMBEDDING_MODEL
)
client = PersistentClient(
    path=r"D:\USER\generative-ai-learning-resources\legal-assistant\RAG\Ollama\law"
)

collection = client.get_or_create_collection(
    name="law", embedding_function=embedding_function
)
chuong_json = JSONLoader(
    file_path=r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\luat-an-ninh-quoc-gia.json",
    jq_schema=".noi_dung[].chuong.ten",
    text_content=False,
)
dieu_json = JSONLoader(
    file_path=r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\luat-an-ninh-quoc-gia.json",
    jq_schema=".noi_dung[].chuong.dieu",
    text_content=False,
)
diem_json = JSONLoader(
    file_path=r"D:\USER\generative-ai-learning-resources\legal-assistant\Data\luat-an-ninh-quoc-gia.json",
    jq_schema=".noi_dung[].chuong.dieu[].diem",
    text_content=False,
)

chuong_doc = chuong_json.load()
dieu_doc = dieu_json.load()
diem_doc = diem_json.load()

collection.add(
    documents=chuong_doc,
    ids=[f"id{i}" for i in range(len(chuong_doc))],
)

# collection.add(
#     documents=dieu_doc,
#     ids=[f"id{i}" for i in range(len(dieu_doc))],
# )

# collection.add(
#     documents=dieu_doc,
#     ids=[f"id{i}" for i in range(len(dieu_doc))],
# )
