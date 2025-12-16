# ЛР9 — «База данных» на CSV: класс Group, CRUD-операции и CLI


# A. Реализовать класс Student (models.py)
```python
import csv
from pathlib import Path
from src.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                f.write("fio,birthdate,group,gpa\n")

    def _read_all(self):
        with open(self.path, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
            # убираем BOM и лишние символы из ключей
            clean_rows = []
            for r in rows:
                clean = {}
                for k, v in r.items():
                    clean[k.strip().replace("\ufeff", "")] = v
                clean_rows.append(clean)
            return clean_rows

    def _write_all(self, rows):
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=["fio", "birthdate", "group", "gpa"]
            )
            writer.writeheader()
            writer.writerows(rows)

    def list(self):
        return [Student.from_dict(r) for r in self._read_all()]

    def add(self, student: Student):
        rows = self._read_all()
        rows.append(student.to_dict())
        self._write_all(rows)

    def find(self, substr: str):
        return [
            Student.from_dict(r)
            for r in self._read_all()
            if substr.lower() in r["fio"].lower()
        ]

    def remove(self, fio: str):
        rows = [r for r in self._read_all() if r["fio"] != fio]
        self._write_all(rows)

    def update(self, fio: str, **fields):
        rows = self._read_all()
        for r in rows:
            if r["fio"] == fio:
                for k, v in fields.items():
                    r[k] = str(v)
        self._write_all(rows)
```

# Тесты
Тест 1. Проверка метода list() — вывод всех студентов из CSV-файла.

Тест 2. Проверка метода add() — добавление нового студента в хранилище.

Тест 3. Проверка метода find() — поиск студента по подстроке в ФИО.

Тест 4. Проверка метода update() — обновление данных существующего студента.

Тест 5. Проверка метода remove() — удаление студента по ФИО.

Тест 6. Проверка корректности CSV-файла — наличие заголовка и сохранение данных после CRUD-операций.
<img width="921" height="526" alt="ЛР 9 1" src="https://github.com/user-attachments/assets/e2e729c7-31c1-4139-bf20-992a21a9ba7f" />
<img width="919" height="212" alt="ЛР 9 2" src="https://github.com/user-attachments/assets/61b7200d-3492-4386-86cd-8c2d19f2a06e" />
<img width="406" height="137" alt="image" src="https://github.com/user-attachments/assets/06f18f87-66f0-4e3b-a563-f6ff534ff451" />



