from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from pymongo import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv()

# Load PDF
loader = PyPDFLoader("2.pdf")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

client = MongoClient("")

db = client["LDRP_RAG"]
collection = db["documents"]

for doc in docs:
    embedding = embeddings.embed_query(doc.page_content)
    document_data ={
        "content" : doc.page_content,
        "embedding" : embedding
    }
    collection.insert_one(document_data)
print("document ingested and embedding stored in MongoDB")



