import random
from src.models.database import Database
from src.models.subject import Subject
from src.utils.validators import is_valid_password
from src.utils.ids import new_subject_id
from src.utils.grading import grade_for, average_mark, is_pass_final

def run_enrolment_menu(student):
    while True:
        try:
            print("\n(c) change password")
            print("(e) enrol")
            print("(r) remove")
            print("(s) show")
            print("(x) exit")
            choice = input("> ").strip().lower()

            if choice == "c":
                _change_password(student)
            elif choice == "e":
                _enrol_subject(student)
            elif choice == "r":
                _remove_subject(student)
            elif choice == "s":
                _show_enrolment(student)
            elif choice == "x":
                break
            else:
                print("Invalid option, try again.")
        except Exception as e:
            print(f'Error! {e}')

def _change_password(student):
    new_pwd = input("Enter new password: ").strip()
    if not is_valid_password(new_pwd):
        print("Invalid password format.")
        return
    # Brief allows reusing same password
    student.password = new_pwd
    Database.save_student(student)
    print("Password updated.")

def _enrol_subject(student):
    if len(student.subjects) >= 4:
        print("You have already enrolled in the maximum of four (4) subjects.")
        return
    existing = {s["id"] for s in student.subjects}
    sid = new_subject_id(existing)
    mark = random.randint(25, 100)
    grade = grade_for(mark)
    new_subject=Subject(sid,mark,grade)
    student.subjects.append(new_subject.to_dict())
    Database.save_student(student)
    print(f"Enrolled in subject {sid} with mark {mark} ({grade}).")

def _remove_subject(student):
    target = input("Enter subject ID to remove: ").strip()
    for i, s in enumerate(student.subjects):
        if s["id"] == target:
            removed = student.subjects.pop(i)
            Database.save_student(student)
            print(f"Removed subject {removed['id']}.")
            return
    print("Subject not found.")

def _show_enrolment(student):
    if not student.subjects:
        print("No subjects enrolled yet.")
    else:
        print("\nEnrolled subjects:")
        for s in student.subjects:
            print(f"- {s['id']}: mark {s['mark']} grade {s['grade']}")
        avg = average_mark(student.subjects)
        print(f"Average mark: {avg}")
        if len(student.subjects) < 4:
            print("Status: in progress (final pass/fail decided at 4 subjects).")
        else:
            print("Status:", "PASS" if is_pass_final(student.subjects) else "FAIL")
