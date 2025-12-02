# ЛР8 – ООП в Python: @dataclass Student, методы и сериализация

# A. Реализовать класс Student (models.py)
```python
from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any

@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {self.birthdate}. Use YYYY-MM-DD")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA must be between 0 and 5, got {self.gpa}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
            
        return age

    def to_dict(self) -> Dict[str, Any]:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Student":
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self) -> str:
        return f"Студент: {self.fio}, Группа: {self.group}, GPA: {self.gpa}, Возраст: {self.age()} лет"

if __name__ == "__main__":
    try:
        student = Student(
            fio="Иванов Иван Иванович",
            birthdate="2000-05-15",
            group="SE-01",
            gpa=4.5
        )
        print(student)
        print(f"Словарь: {student.to_dict()}")
    except ValueError as e:
        print(f"Ошибка: {e}")

```
<img width="583" height="71" alt="image" src="https://github.com/user-attachments/assets/4a74f061-6de7-4055-bd3a-bfeaadba9085" />

# B. Реализовать модуль serialize.py
import json
import os
from typing import List
from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    """Сохраняет список студентов в JSON файл"""
    data = [student.to_dict() for student in students]
    
    # Создаём папки если их нет
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> List[Student]:
    """Загружает список студентов из JSON файла"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        students = []
        for item in data:
            try:
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при создании студента: {e}")
                continue
                
        return students
    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON: {path}")
        return []

if __name__ == "__main__":
    print("=== Тест ЛР8 ===")
    
    # 1. Создаём студентов
    students = [
        Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.5),
        Student("Петрова Анна Сергеевна", "2001-08-22", "SE-02", 3.8),
        Student("Сидоров Алексей Петрович", "1999-12-10", "SE-01", 4.2)
    ]
    
    print("1. Создано 3 студента")
    for s in students:
        print(f"   - {s}")
    
    # 2. Сохраняем в data/lab08/
    output_path = "data/lab08/students_output.json"
    students_to_json(students, output_path)
    print(f"2. Сохранено в: {output_path}")
    
    # 3. Загружаем из data/lab08/
    input_path = "data/lab08/students_input.json"
    print(f"3. Загружаем из: {input_path}")
    
    if os.path.exists(input_path):
        loaded_students = students_from_json(input_path)
        print(f"   Загружено студентов: {len(loaded_students)}")
        for s in loaded_students:
            print(f"   - {s}")
    else:
        print(f"   Файл {input_path} не найден!")
        print("   Создайте его с данными студентов")
    
    print("=== Тест завершён ===")
<img width="470" height="88" alt="image" src="https://github.com/user-attachments/assets/ba0fce5e-f56c-4668-abb3-4617de73d577" />
<img width="312" height="308" alt="image" src="https://github.com/user-attachments/assets/76792c67-2a0e-4ee0-9518-994a1977c572" />
<img width="307" height="308" alt="image" src="https://github.com/user-attachments/assets/97a42695-e79a-48dd-9b4a-1e63846bfa7e" />





