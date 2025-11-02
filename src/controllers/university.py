from src.controllers.student import run_student_menu
from src.controllers.admin import run_admin_menu
from src.view.student_gui_view import run_student_gui_main
def run_university_menu():
    while True:
        try:
            print("\n(A) Admin")
            print("(S) Student")
            print("(G) GUI for Student")
            print("(X) Exit")
            choice = input("> ").strip().upper()

            if choice == "A":
                run_admin_menu()
            elif choice == "S":
                run_student_menu()
            elif choice == "G":
                run_student_gui_main()
            elif choice == "X":
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")
        except Exception as e:
            print(f'Error! {e}')
