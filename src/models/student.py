class Student:
    def __init__(self, id, name, email, password, subjects=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects or []  # list of dicts: {"id": "123", "mark": 88, "grade": "HD"}

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": self.subjects,
        }

    @staticmethod
    def from_dict(d: dict) -> "Student":
        return Student(
            id=d["id"],
            name=d["name"],
            email=d["email"],
            password=d["password"],
            subjects=d.get("subjects", []),
        )

class Student:
    def __init__(self, id, name, email, password, subjects=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects or []  # list of dicts: {"id": "123", "mark": 88, "grade": "HD"}

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": self.subjects,
        }

    @staticmethod
    def from_dict(d: dict) -> "Student":
        return Student(
            id=d["id"],
            name=d["name"],
            email=d["email"],
            password=d["password"],
            subjects=d.get("subjects", []),
        )
