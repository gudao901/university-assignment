from src.models.database import Database
from src.models.student import Student
from src.utils.ids import new_student_id
from src.utils.validators import is_valid_email, is_valid_password


def login(view_info,on_success,on_failure):
    login_name=view_info.emailText.get().lower()
    login_password=view_info.passwordText.get()
    students=Database.read_all_students()
    for student in students:
        if (login_name==student.id or login_name==student.email.lower()) and login_password==student.password:
            on_success(student)
            return True
    on_failure("Login Error: Student ID / Email or Password is incorrect!")
    return False

    
def register(view_info,on_success,on_failure):
    name=view_info.nameText.get()
    email=view_info.emailText.get().lower()
    password=view_info.passwordText.get()
    if not is_valid_email(email):
        on_failure('Email Error: Email should be in the format of "@university.com"')
        return False   
    if not is_valid_password(password):
        on_failure("Password Error: Password should start with an upper-case letter, at least five (5) letters, followed by three (3) or more digits")
        return False
    if password!=view_info.password2Text.get():
        on_failure("Password Error: Password does not match!")
        return False
    # end verify pattern, begin verfy the same of email
    #read students data newest
    students=Database.read_all_students()
    if any(s.email == email for s in students):
        on_failure(f"Email Error: Email {email} has been registered!")
        return False
    #get the newest data for update
    new_id = new_student_id({s.id for s in students})
    new_student = Student(new_id, name, email, password)
    students.append(new_student)
    #save all
    Database.write_all_students(students)
    on_success(f"Register successfully! Your student info is {new_student}, please remember it!")

def password_confirm(view_info,on_success,on_failure):
    current_password=view_info.currentText.get()
    new_password=view_info.newText.get()
    if current_password==view_info.student.password:
        if is_valid_password(new_password):
            if new_password==view_info.new2Text.get():
                view_info.student.password=new_password
                Database.save_student(view_info.student)
                on_success('Password update successfully, please remember it!')
            else:
                on_failure('New password entries do not match!')   
        else:
            on_failure('Password format error: the first character must be uppercase letter, followed by at least 4 letters and ends with at least 3 digits!')
    else:
        on_failure('Current password incorrect!')