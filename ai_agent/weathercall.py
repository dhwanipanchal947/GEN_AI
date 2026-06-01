from langchain_openai import ChatOpenAI         #langchain ae frame work chr 
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv('OPENAI_API_KEY')
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant."),
        ("user","give a current weather of {city} ")
    ]
)
chain = prompt | client

response = chain.invoke({
    "city": input("Enter a city name: ")
})
print(response.content)
 #ama content km lakhue ke response ame nem sarkha formate ma na ape atle 
 #sarkha formate mAte agad apde json and string method use kari che.
#invoke method ae direct aek sathe j akhu output api de che .