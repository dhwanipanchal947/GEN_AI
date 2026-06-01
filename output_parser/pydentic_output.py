from fastapi import FastAPI                                    #install karva karva = pip install fastapi uvicorn
from pydantic import BaseModel                                 #install karva  = pip install fastapi pyndantic uvicorn
from langchain_openai import ChatOpenAI                        #langchain ae frame work chr 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
import os
   # run karva = uvicorn filemane:app --reload


load_dotenv()

app = FastAPI()

que = []
#-----------------openai-----------------------------------------------------------------------------------------------------------------

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv('OPENAI_API_KEY')
)

#----------------------model----------------------------------------------------------------------------------------------------------------
class questionpaperbody(BaseModel):
    topic: str
    totalmarks: str
    questiontype: str
    marksperquestion : int

class question(BaseModel):
    question: str
    options: list[str]
    answer: str
    
class questionpaper(BaseModel):
    topic: str
    passing_marks: int
    questions: list[question]
   
#===========================API================================================================================================================
Parser = PydanticOutputParser(pydantic_object=questionpaper)              #variable is yellow colour

# CREATE
@app.post("/questionpaperGenerator/")
async def create_papers(papers: questionpaperbody):

    prompt = ChatPromptTemplate.from_messages([
        ("system", "you are a question paper generator,{format}."),
        ("user","genrate a question paper with{questiontype} question on {topic} marks as {marks} questiontype {questiontype} marks as per question {marksperquestion} and give a answer")
    ])

    chain = prompt | llm | Parser

    response = chain.invoke(
    {
        "topic": papers.topic,
        "marks": papers.totalmarks,
        "questiontype":papers.questiontype,
        "marksperquestion" : papers.marksperquestion,
        "format" :Parser.get_format_instructions()
    })

    # sring formate in terminal
    print("\n ========== question paper=========\n")
    print(response)

    #json formate
    return{
        "topic" : papers.topic,
        "questiontype": papers.questiontype,
        "questionpaper" : response
    }