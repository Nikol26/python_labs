# test_lab8_working.py
import os
import sys

# Добавляем src/lab08 в путь
sys.path.insert(0, 'src/lab08')

from models import Student
from serialize import students_to_json, students_from_json

print("=" * 50)
print("РАБОЧИЙ ТЕСТ ЛР8")
print("=" * 50)

# Проверяем текущую папку
print(f"Текущая папка: {os.getcwd()}")

# 1. Тест Student
print("\n1. Тестируем класс Student:")
s = Student("Тестовый Студент", "2000-01-01", "SE-01", 4.0)
print(f"   Создан: {s}")
print(f"   Возраст: {s.age()}")
print(f"   Словарь: {s.to_dict()}")

# 2. Тест сериализации
print("\n2. Тестируем сериализацию:")
test_students = [s]
test_file = "data/lab08/test_working.json"
students_to_json(test_students, test_file)
print(f"   Файл создан: {os.path.exists(test_file)}")

# 3. Тест десериализации
print("\n3. Тестируем десериализацию:")
if os.path.exists("data/lab08/students_input.json"):
    loaded = students_from_json("data/lab08/students_input.json")
    print(f"   Загружено студентов: {len(loaded)}")
    for i, student in enumerate(loaded, 1):
        print(f"   {i}. {student}")
else:
    print("   Файл students_input.json не найден!")

print("\n" + "=" * 50)
print("ТЕСТ ЗАВЕРШЁН")
print("=" * 50)
