from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser

import os

# Load ENV variables
load_dotenv()

# FastAPI app
app = FastAPI()

# OpenAI Client
client = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

# -----------------------------
# INPUT MODEL
# -----------------------------

class ProjectDocumentBody(BaseModel):
    project_name: str
    technology: str
    project_type: str


# -----------------------------
# OUTPUT MODELS
# -----------------------------

class ProjectDocument(BaseModel):
    project_name: str
    summary: str
    description: str
    modules: list[str]
    workflow: list[str]
    technology_stack: list[str]
    database: str
    conclusion: str


# -----------------------------
# OUTPUT PARSER
# -----------------------------

parser = PydanticOutputParser(pydantic_object=ProjectDocument)

# -----------------------------
# PROMPT TEMPLATE
# -----------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert Project Document Generator.

            Generate professional project documentation.

            {format}
            """
        ),
        (
            "user",
            """
            Generate a complete project document.

            Project Name: {project_name}

            Technology Used: {technology}

            Project Type: {project_type}

            Include:
            - Summary
            - Description
            - Modules
            - Workflow
            - Technology Stack
            - Database
            - Conclusion
            """
        )
    ]
)

# -----------------------------
# CHAIN
# -----------------------------

chain = prompt | client | parser


# -----------------------------
# API
# -----------------------------

@app.post("/project-document-generator/")
def generate_project_document(project: ProjectDocumentBody):

    response = chain.invoke(
        {
            "project_name": project.project_name,
            "technology": project.technology,
            "project_type": project.project_type,
            "format": parser.get_format_instructions()
        }
    )

    print("Project Document")
    print(response)

    return {
        "message": "Project document generated successfully",
        "data": response
    }