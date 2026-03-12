from flask import Flask, jsonify, request
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)

students = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Thameem"},
    {"id": 3, "name": "Suresh"},
    {"id": 4, "name": "Ramesh"},
    {"id": 5, "name": "Suresh"},
    {"id": 6, "name": "Suresh"},
]

@app.route("/")
def home():
    return "Flask REST API Running"

@app.route("/students", methods=["GET"])
def get_students():
    # """
    # Get All Students
    # ---
    # responses:
    #   200:
    #     description: Returns list of students
    # """
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():
    new_student = request.json
    students.append(new_student)
    return jsonify({
        "message": "Student added successfully",
        "student": new_student
    }), 201



@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    for student in students:
        if student["id"] == id:
            student["name"] = request.json["name"]
            return jsonify({"message": "Student updated"})
    return jsonify({"message": "Student not found"})

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    global students
    students = [student for student in students if student["id"] != id]
    return jsonify({"message": "Student deleted"})

if __name__ == "__main__":
    app.run(debug=True)