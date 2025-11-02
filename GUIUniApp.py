from src.view.student_gui_view import run_student_gui_main
from src.models.database import Database

def main():
    # Create students.data on first run
    Database.ensure_file()
    # Start the app
    run_student_gui_main()

if __name__ == "__main__":
    main()


