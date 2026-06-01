from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()       #FastAPI application બનાવે છે.

expenses = []
expense_id_counter = 1


class Expense(BaseModel):
    expense_name: str
    expense_type: str
    expense_description: str
    expense_price: float
    expense_payment_type: str


# CREATE
@app.post("/expenses/")
def create_expense(expense: Expense):

    global expense_id_counter
                                                # Pydantic object ને Python dictionary માં convert કરે છે. 
    new_expense = expense.dict()               #Convert Object to Dictionary dict ma data ni value store thay 
    new_expense["expense_id"] = expense_id_counter

    expense_id_counter += 1

    expenses.append(new_expense)

    return {
        "msg": "Expense added successfully",
        "data": new_expense
    }


# GET ALL
@app.get("/expenses/")
def get_all_expenses():

    return {
        "msg": "Expenses retrieved successfully",
        "data": expenses
    }


# GET by id
@app.get("/expenses/{expense_id}")
def get_single_expense(expense_id: int):

    for expense in expenses:              # દરેક expense check કરે છે.
 
        if expense["expense_id"] == expense_id:      #ID match થાય તો return કરે છે
            return expense

    return {
        "msg": "Expense not found"
    }


# UPDATE
@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated_expense: Expense):

    for index, expense in enumerate(expenses):                          #અહીં:index = position expense = actual record

        if expense["expense_id"] == expense_id:

            expenses[index]["expense_name"] = updated_expense.expense_name
            expenses[index]["expense_type"] = updated_expense.expense_type
            expenses[index]["expense_description"] = updated_expense.expense_description
            expenses[index]["expense_price"] = updated_expense.expense_price
            expenses[index]["expense_payment_type"] = updated_expense.expense_payment_type

            return {
                "msg": "Expense updated successfully",
                "data": expenses[index]
            }

    return {
        "msg": "Expense not found"
    }


# DELETE SINGLE expense
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    for index, expense in enumerate(expenses):      #enumerate is a function .List ના item અને તેનો index બંને આપે છે.
        if expense["expense_id"] == expense_id:

            deleted_expense = expenses.pop(index)

            return {
                "msg": "Expense deleted successfully",
                "data": deleted_expense
            }

    return {
        "msg": "Expense not found"
    }


# DELETE ALL
@app.delete("/expenses/")
def delete_all_expenses():

    expenses.clear()

    return {
        "msg": "All expenses deleted successfully",
        "data": expenses
    }
#run karva mate : uvicorn project:app --reload