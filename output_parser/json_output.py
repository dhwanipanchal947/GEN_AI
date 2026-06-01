from fastapi import FastAPI                                    #install karva karva = pip install fastapi uvicorn
from pydantic import BaseModel                                 #install karva  = pip install fastapi pyndantic uvicorn
from langchain_openai import ChatOpenAI                        #langchain ae frame work chr 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser     #output formate change karva 
from dotenv import load_dotenv
import os
   # run karva = uvicorn filemane:app --reload


load_dotenv()

app = FastAPI()

que = []


#-----------------openai-------------------

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv('OPENAI_API_KEY')
)

#----------------------model----------------------------
class paper(BaseModel):
    topic: str
    totle_marks: float
    question_type: str
    marks_per_question : float
   

# CREATE only
@app.post("/questionpaperGenerator/")
def create_papers(papers: paper):

    prompt = ChatPromptTemplate.from_messages([
        ("system", "you are a question paper genrator. give answer in json format"),
        ("user","genrate a question paper with{questiontype} question on {topic} marks as {marks} questiontype {questiontype} marks as per question {marksperquestion} and give a answer.")
    ])

    parser = JsonOutputParser()

    chain = prompt | llm | parser

    response = chain.invoke({
        "topic": papers.topic,
        "marks": papers.totle_marks,
        "questiontype":papers.question_type,
        "marksperquestion" : papers.marks_per_question
    })
    # sring formate in terminal
    print("\n ========== question paper=========\n")
    print(response)

    #json formate
    return{
        "topic" : papers.topic,
        "questiontype": papers.question_type,
        "questionpaper" : response
    }