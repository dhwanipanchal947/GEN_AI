from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_keys= os.getenv("OPENAI_API_KEY")

)

arr = [
    ("system","you are a helpfull assistant"),
]

for i in range(5):
    x = input("enter your query:")
    arr.append(("user",x))
    prompt = ChatPromptTemplate.from_messages(
        arr
    )
    chain = prompt | client
    response = chain.invoke({})
    arr.append(("ai",response.content))
    print(response.content)