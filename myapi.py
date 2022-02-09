from fastapi import FastAPI

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 19,
        "class": "Freshman"
    },
    2: {
        "name": "Praveen",
        "age": 42,
        "class": "MBA"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

