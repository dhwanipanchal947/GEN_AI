#---API બનાવવા માટે framework.-----
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()   # FastAPI application object બનાવે છે.


stu = []

class Students(BaseModel):
    Course: str
    name:str
    Enrollment:int
    is_deleted : bool



@app.post("/PostStudent/")
def create_student(student: Students):  # Student data receive કરે છે.
    stu.append(student.dict())
    return{
        "msg":"student added successfully",
        "data": stu
    }


@app.get("/getStudent/")
def get_student():
    return{
        "msg":"student data retrieved successfully",
        "data": stu
    }


@app.get("/getStudentById/{Enrollment}")
def get_student_by_id(Enrollment : int):
    for student in stu:
        if student["Enrollment"]== Enrollment:
            return {
                "msg": "student data by id",
                "data":student
            }
    return {
        "msg": "student not found"
    }



@app.put("/PutStudent/{Enrollment}")
def update(Enrollment : int , updated_student: Students):
    for student in stu:
        if student["Enrollment"]== Enrollment:
            student["name"]= updated_student.name
            student["Course"]= updated_student.Course
            return{
                "msg":"student data update successfully",
                "data": student
            }
    return{
        "msg":"student not found"
    }


@app.delete("/DeleteStudent/{Enrollment}")
def delete_student(Enrollment: int):
    for student in stu:
        if student["Enrollment"]==Enrollment:
            stu.remove(student)                             #Student list માંથી permanently remove થાય છે.DATABASE MA THI BI JAY 
            return{
                "msg":"student data deleted successfully",
                "data":stu
            }
    return{
        "msg":"student not found"
    }

@app.delete("/deleteAllStudents/")
def delete_all_student():
    stu.clear()                                  #સંપૂર્ણ list empty કરી દે છે.
    return {
        "msg": "all students deleted successfully"
    }
    
# SOFT DELETE

@app.delete("/SoftDeleteStudent/{Enrollment}")
def soft_delete_student(Enrollment: int):

    for student in stu:

        if student["Enrollment"] == Enrollment:

            student["is_deleted"] = True           #Student delete થતો નથી.માત્ર flag change થાય છે.

            return {
                "msg": "student soft deleted successfully",
                "data": student
            }

    return {
        "msg": "student not found"
    }

#Soft Delete માં record database માંથી delete થતો નથી. 
# માત્ર is_deleted=True flag set થાય છે જેથી future માં data recover કરી શકાય. Hard Delete માં record permanently remove થઈ જાય છે.