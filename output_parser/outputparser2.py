#FASTAPI VADAR PYDENTIC MA OUTPUT LAVA MATE AA USEFUL CHE 

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")


# Question Model
class Question(BaseModel):
    question: str
    options: list[str]
    answer: str


# Question Paper Model
class QuestionPaper(BaseModel):
    topic: str
    passing_score: int
    questions: list[Question]


# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a question paper generator. {format}"
        ),
        (
            "user",
            "Generate a question paper for topic {topic} with question type {question_type} and number of questions {num_questions}"
        )
    ]
)

# Parser
parser = PydanticOutputParser(pydantic_object=QuestionPaper)

# Chain
chain = prompt | llm | parser

# Invoke
response = chain.invoke({
    "topic": "physics",
    "question_type": "mcq",
    "num_questions": 5,
    "format": parser.get_format_instructions()
})

print(response)