from langchain_openai import ChatOpenAI
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
        ("user","create a question paper on topic {topic},of marks {marks} and difficulty level {difficulty}")
    ]
)
chain = prompt | client
response = chain.stream(
    {
        "topic": input("ent a topic : "),
        "marks": int(input("ent a marks: ")),
        "difficulty": input("ent a difficulty level : ")
    }
)
for chunk in response:
    print(chunk.content, end="")
    
# stream method ae jem jem genrate thaya kare aem aem output ape .