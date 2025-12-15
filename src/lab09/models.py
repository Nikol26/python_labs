class Student:
    def __init__(self, fio, birthdate, group, gpa):
        self.fio = fio
        self.birthdate = birthdate
        self.group = group
        self.gpa = float(gpa)
    
    def to_dict(self):
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": str(self.gpa)
        }
    
    @classmethod
    def from_dict(cls, data):
        fio_key = "fio"
        if "\ufefffio" in data:
            fio_key = "\ufefffio"
        
        return cls(
            fio=data[fio_key],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
