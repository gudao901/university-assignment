class Subject:
    def __init__(self, id, mark, grade):
        self.id = id
        self.mark = mark
        self.grade = grade
 
    def to_dict(self):
        return {
            "id": self.id,
            "mark": self.mark,
            "grade": self.grade,
        }

    @staticmethod
    def from_dict(d: dict) -> "Subject":
        return Subject(
            id=d["id"],
            mark=d["mark"],
            grade=d["grade"],
        )
    def __str__(self):
        return f'Subject ID: {self.id}, mark: {self.mark}, grade: {self.grade}'
