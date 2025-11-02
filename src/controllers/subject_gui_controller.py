import random
from src.models.database import Database
from src.models.subject import Subject
from src.utils.ids import new_subject_id
from src.utils.grading import grade_for

#initial the frame of Subject GUI (student enrol ,remove subject and change password)
def subject_enrol(view_info,on_success,on_failure):
    if len(view_info.student.subjects)<4:
        existing = {s["id"] for s in view_info.student.subjects}
        sid = new_subject_id(existing)
        mark = random.randint(25, 100)
        grade = grade_for(mark)
        view_info.student.subjects.append(Subject(sid,mark,grade).to_dict())
        Database.save_student(view_info.student)
        on_success(f'Enrol Subject {sid} successfully!')
    else:
        on_failure('Enrol Subject Error: Your subject selection hit the limit! Subjects capacity:4')
    
def subject_remove(view_info,id,on_success):
    for i, s in enumerate(view_info.student.subjects):
        if s["id"] == id:
            view_info.student.subjects.pop(i)
            Database.save_student(view_info.student)
    Database.save_student(view_info.student)
    on_success(f'Remove Subject {id} successfully!')


