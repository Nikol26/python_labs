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
            return list(csv.DictReader(f))

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

    def stats(self):
        students = self.list()
        gpas = [s.gpa for s in students]

        groups = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1

        top = sorted(students, key=lambda s: s.gpa, reverse=True)[:5]

        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups,
            "top_5_students": [
                {"fio": s.fio, "gpa": s.gpa} for s in top
            ]
        }
