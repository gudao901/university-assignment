import os, json
from src.models.student import Student

class Database:
    FILE_PATH = "students.data"

    @staticmethod
    def ensure_file():
        if not os.path.exists(Database.FILE_PATH):
            with open(Database.FILE_PATH, "w") as f:
                json.dump([], f)
            print("[System] Created students.data")

    @staticmethod
    def read_all_students():
        if not os.path.exists(Database.FILE_PATH):
            return []
        with open(Database.FILE_PATH, "r") as f:
            try:
                data = json.load(f)
                return [Student.from_dict(d) for d in data]
            except json.JSONDecodeError:
                return []

    @staticmethod
    def write_all_students(students):
        with open(Database.FILE_PATH, "w") as f:
            json.dump([s.to_dict() for s in students], f, indent=2)

    @staticmethod
    def clear():
        with open(Database.FILE_PATH, "w") as f:
            json.dump([], f)

import os, json
from src.models.student import Student

class Database:
    FILE_PATH = "students.data"

    @staticmethod
    def ensure_file():
        if not os.path.exists(Database.FILE_PATH):
            with open(Database.FILE_PATH, "w") as f:
                json.dump([], f)
            print("[System] Created students.data")

    @staticmethod
    def read_all_students():
        if not os.path.exists(Database.FILE_PATH):
            return []
        with open(Database.FILE_PATH, "r") as f:
            try:
                data = json.load(f)
                return [Student.from_dict(d) for d in data]
            except json.JSONDecodeError:
                return []

    @staticmethod
    def write_all_students(students):
        with open(Database.FILE_PATH, "w") as f:
            json.dump([s.to_dict() for s in students], f, indent=2)

    @staticmethod
    def clear():
        with open(Database.FILE_PATH, "w") as f:
            json.dump([], f)

    @staticmethod
    def save_student(updated_student):
        """Replace a student by id and persist."""
        students = Database.read_all_students()
        for i, s in enumerate(students):
            if s.id == updated_student.id:
                students[i] = updated_student
                break
        else:
            students.append(updated_student)  # if not found, add
        Database.write_all_students(students)
