# pip install langchain_community langchain_text_splitters pymongo     aa 3 ae dow 
# pip list  kai kai library download che a ejova mate use thay.
# then also  pip install pypdf download kaea
 # ----------------ingestion meaning add karvu.--------------







from langchain_community.document_loaders import PyPDFLoader           #PDF વાંચવા
from langchain_text_splitters import RecursiveCharacterTextSplitter    #Text ને chunks માં વહેંચવા
from langchain_openai import OpenAIEmbeddings                   #Text ને vector માં convert કરવા
from dotenv import load_dotenv                               #API key load કરવા
from pymongo import MongoClient                                  #MongoDB connect કરવા
import os

# Load .env file
load_dotenv()

# Load PDF
loader = PyPDFLoader("1.pdf")
documents = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,            #chunk માં લગભગ 500 characters રહેશે.
    chunk_overlap=100          #chunk ના 100 characters આગળના chunk માં ફરી આવશે.
)

docs = text_splitter.split_documents(documents)

# OpenAI Embeddings
embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

# MongoDB Connection
client = MongoClient(
    "mongodb+srv://admin:admin@cluster0.t4paro1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

db = client["LDRP_RAG"] #database name 
collection = db["documents"] # table name 

for doc in docs:                       #એક પછી એક chunk process થશે.
    embedding = embeddings.embed_query(doc.page_content)        # embedding kare text nu je split karya hoy ne ena embedding etle vector form karvu 
    document_data ={                           # embeddding karelo data store kare 
        "text" : doc.page_content,
        "embedding" : embedding
    }
    collection.insert_one(document_data)            # varafara thi split karela text ne add karti jaay 
print("document ingested and embedding stored in MongoDB")





# ama document ni loader ma store karai ne text splitter thi aene nana parts ma devide karva ni
# che then pai tene vectort ma convert karva nu atle llm no use thse atle openai lesu aene 
# emmbeding kevay have pymongo add karsu je mongo db sathe connect kare  HAVE AGAD DOCS MA APDU 
# SAVE HATU have database create karyo aema db nu mane apue have data base ma table banavue 
#documents kari ne have loop fervue vector leva )documents leva mate) and pai aene store kar
#didhu  and je dictionary banavi aene connect karue 