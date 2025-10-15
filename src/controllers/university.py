from src.controllers.student import run_student_menu
from src.controllers.admin import run_admin_menu

def run_university_menu():
    while True:
        print("\n(A) Admin")
        print("(S) Student")
        print("(X) Exit")
        choice = input("> ").strip().upper()

        if choice == "A":
            run_admin_menu()
        elif choice == "S":
            run_student_menu()
        elif choice == "X":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
