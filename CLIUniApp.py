from src.controllers.university import run_university_menu
from src.models.database import Database

def main():
    # Create students.data on first run
    Database.ensure_file()
    # Start the app
    run_university_menu()

if __name__ == "__main__":
    main()
