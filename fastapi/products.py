from fastapi import FastAPI       # fastapu is web framework for building APIs using Python
from pydantic import BaseModel   # pydantic is makes it nearly as fast as Node.js and Go APIs. basemodel na data sacha che ke nai check karva mate.


app = FastAPI() #FastAPI application નો object બનાવે છે. બધા routes (GET, POST) આ app સાથે જોડાય છે

products=[]    #Products temporary memory માં store થાય છે.

class product(BaseModel):       #Product માટે schema/model છે.
    name:str
    price:int
    id:int
    quantity:int

@app.post("/Postproduct/")           #POST request handle કરે છે.
def add_product(product: product):
    products.append(product.dict())
    return{
        "msg" :"STudent added successfully",
        "data": products
    }

@app.get("/getproduct/")
def get_product():
    return{
        "msg" :"STudent retrived successfully",
        "data": products
    }

# run karva mate uvicorn file:app --reload
