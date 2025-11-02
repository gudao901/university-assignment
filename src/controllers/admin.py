from src.models.database import Database
from src.utils.grading import grade_for, average_mark, is_pass_final

def run_admin_menu():
    while True:
        try:
            print("\n(c) clear database")
            print("(g) group students")
            print("(p) partition students")
            print("(r) remove student")
            print("(s) show")
            print("(x) exit")
            choice = input("> ").strip().lower()

            if choice == "c":
                _clear_database()
            elif choice == "g":
                _group_students()
            elif choice == "p":
                _partition_students()
            elif choice == "r":
                _remove_student()
            elif choice == "s":
                _show_students()
            elif choice == "x":
                break
            else:
                print("Invalid option, try again.")
        except Exception as e:
            print(f'Error! {e}')


def _show_students():
    students = Database.read_all_students()
    if not students:
        print("No students found.")
        return

    print("\nAll students:")
    for s in students:
        subj_count = len(s.subjects)
        avg = average_mark(s.subjects) if subj_count else 0.0
        print(f"- ID {s.id} | {s.name} | {s.email} | subjects: {subj_count} | avg: {avg}")


def _group_students():
    students = Database.read_all_students()
    if not students:
        print("No students found.")
        return

    buckets = {"HD": [], "D": [], "C": [], "P": [], "F": [], "N/A": []}
    for s in students:
        if s.subjects:
            avg = average_mark(s.subjects)
            g = grade_for(int(round(avg)))
        else:
            g = "N/A"
        buckets.setdefault(g, []).append(s.id)

    print("\nGrouped by grade:")
    for g in ["HD", "D", "C", "P", "F", "N/A"]:
        ids = buckets.get(g, [])
        print(f"{g}: {', '.join(ids) if ids else '-'}")

def _partition_students():
    students = Database.read_all_students()
    if not students:
        print("No students found.")
        return

    passed = []
    failed = []
    for s in students:
        if is_pass_final(s.subjects):   # PASS only if 4 subjects and avg >= 50
            passed.append(s.id)
        else:
            failed.append(s.id)

    print("\nPASS:")
    print(", ".join(passed) if passed else "-")
    print("FAIL:")
    print(", ".join(failed) if failed else "-")


def _remove_student():
    students = Database.read_all_students()
    sid = input("Enter student ID to remove: ").strip()
    new_list = [s for s in students if s.id != sid]

    if len(new_list) == len(students):
        print("Student not found.")
        return

    Database.write_all_students(new_list)
    print(f"Removed student {sid}.")


def _clear_database():
    confirm = input("Are you sure you want to clear all students? (y/n): ").strip().lower()
    if confirm == "y":
        Database.clear()
        print("All student data cleared.")
    else:
        print("Cancelled.")
