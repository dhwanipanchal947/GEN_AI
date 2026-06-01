# API USE VAGAR AA JSON MA OUTPUT PARSER VADO PROGRAM  CHE

from langchain_openai import ChatOpenAI                        #langchain ae frame work chr 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser     #output formate change karva 
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_messages([
    ("system","you are a question paper generator. give me output in JSON format."),
    ("user", "generate a que paper for the topic {topic} with questions of type {question_type} difficulty level {difficulty_level} and give a num of questions{num_questions} ")
]
)

parser = JsonOutputParser()

chain = prompt | llm | parser

response = chain.invoke({
    "topic" : "mathematics",
    "question_type" : "mcq",
    "difficulty_level" : "medium",
    "num_questions" : 5
})