from src.utils.validators import is_valid_email, is_valid_password
from src.models.database import Database
from src.models.student import Student
from src.utils.ids import new_student_id
from src.controllers.enrolment import run_enrolment_menu

def run_student_menu():
    while True:
        print("\n(l) login")
        print("(r) register")
        print("(x) exit")
        choice = input("> ").strip().lower()

        if choice == "l":
            login()
        elif choice == "r":
            register()
        elif choice == "x":
            break
        else:
            print("Invalid option, try again.")

def register():
    students = Database.read_all_students()

    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    if not is_valid_email(email):
        print("Invalid email format. Must end with @university.com")
        return
    if not is_valid_password(password):
        print("Invalid password format.")
        return

    if any(s.email == email for s in students):
        print("Student already exists.")
        return

    new_id = new_student_id({s.id for s in students})
    new_student = Student(new_id, name, email, password)
    students.append(new_student)
    Database.write_all_students(students)
    print(f"Registration successful! Your ID is {new_id}")

def login():
    students = Database.read_all_students()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    for s in students:
        if s.email == email and s.password == password:
            print(f"Welcome back, {s.name}!")
            run_enrolment_menu(s)   # will build this next
            return

    print("Invalid credentials.")

from src.utils.validators import is_valid_email, is_valid_password
from src.models.database import Database
from src.models.student import Student
from src.utils.ids import new_student_id
from src.controllers.enrolment import run_enrolment_menu

def run_student_menu():
    while True:
        print("\n(l) login")
        print("(r) register")
        print("(x) exit")
        choice = input("> ").strip().lower()

        if choice == "l":
            login()
        elif choice == "r":
            register()
        elif choice == "x":
            break
        else:
            print("Invalid option, try again.")

def register():
    students = Database.read_all_students()

    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    if not is_valid_email(email):
        print("Invalid email format. Must end with @university.com")
        return
    if not is_valid_password(password):
        print("Invalid password format.")
        return
    if any(s.email == email for s in students):
        print("Student already exists.")
        return

    new_id = new_student_id({s.id for s in students})
    new_student = Student(new_id, name, email, password)
    students.append(new_student)
    Database.write_all_students(students)
    print(f"Registration successful! Your ID is {new_id}")

def login():
    students = Database.read_all_students()
    email = input("Enter your email: ").strip()
    password = input("Enter your password: ").strip()

    for s in students:
        if s.email == email and s.password == password:
            print(f"Welcome back, {s.name}!")
            run_enrolment_menu(s)   # next step we’ll implement
            return

    print("Invalid credentials.")
