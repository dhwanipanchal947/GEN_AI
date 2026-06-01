from dotenv import load_dotenv                                  #API Key load કરવા
from langchain_openai import OpenAIEmbeddings ,ChatOpenAI          #Query embedding બનાવવા ,Answer generate કરવા
from pymongo import MongoClient
from langchain_mongodb import MongoDBAtlasVectorSearch           #Vector Search કરવા
import os

load_dotenv()

client = MongoClient(
    "mongodb+srv://admin:admin@cluster0.t4paro1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

db = client["LDRP_RAG"]
collection = db["documents"]

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

# vactor search no upyog karsu retrive mate.MongoDB ને vector database તરીકે use કરવું.

vector_store = MongoDBAtlasVectorSearch(
    collection = collection,
    embedding = embeddings,
    index_name = "RAG_INDEX"
)

query = "How many topics are covered in this PDF? "

ans = vector_store.similarity_search(query=query, k=3)

context = " ".join(
    doc.page_content for doc in ans
)

prompt = f"""

answer only based on the following in the context.

if answer is not found in the context,say you don't know.

context : {context}
question : {query}

"""

llm = ChatOpenAI(                         # LLM initialize થાય છે.અહીં API key explicitly નથી આપી.
    model = "gpt-3.5-turbo"
)

response = llm.invoke(prompt)          #Prompt OpenAI model ને મોકલાય છે.
print("answer:",response.content)


# Complete RAG Architecture:

# PDF Notes
#     ↓
# Loader
#     ↓
# Text Splitter
#     ↓
# Embeddings
#     ↓
# FAISS Vector DB
#     ↓
# Retriever
#     ↓
# Relevant Chunks
#     ↓
# LLM (GPT)
#     ↓
# Final Answer