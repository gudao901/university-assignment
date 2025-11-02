import random

def new_student_id(existing_ids: set[str]) -> str:
    while True:
        n = random.randint(1, 999_999)
        sid = f"{n:06d}"
        if sid not in existing_ids:
            return sid
        
def new_subject_id(existing_ids: set[str]) -> str:
    while True:
        n = random.randint(1, 999)
        sid = f"{n:03d}"
        if sid not in existing_ids:
            return sid
