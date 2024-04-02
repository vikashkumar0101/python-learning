from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "12th Year"

    },
    2: {
        "name": "Rocky",
        "age": 10,
        "year": "10th Year"
    }
}


class Student(BaseModel):
    name = str
    age = int
    year = str


@app.get("/")
def index():
    return {"name": "First Name"}


@app.get("/get-student/{student_id}")  # path parameters
def get_student(*, student_id: int):
    return students[student_id]


@app.get("/get-by-name/{student_id}")  # query parameters and path parameters are combined here
def get_student(*, student_id, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Studen_exixts"}

    students[student_id] = student
    return students[student_id]
