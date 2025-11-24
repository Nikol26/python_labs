import json
import csv
import os


def json_to_csv(src_path: str, dst_path: str):
    if not src_path.lower().endswith(".json"):
        raise ValueError("Исходный файл не является JSON файлом")

    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Файл {src_path} не найден")

    if os.path.getsize(src_path) == 0:
        raise ValueError("JSON файл пустой")

    try:
        with open(src_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Некорректный JSON формат")

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if len(data) == 0:
        raise ValueError("JSON список пустой")

    with open(dst_path, "w", encoding="utf-8", newline="") as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


def csv_to_json(src_path: str, dst_path: str):
    if not src_path.lower().endswith(".csv"):
        raise ValueError("Исходный файл не является CSV файлом")

    if not os.path.exists(src_path):
        raise FileNotFoundError(f"Файл {src_path} не найден")

    if os.path.getsize(src_path) == 0:
        raise ValueError("CSV файл пустой")

    try:
        with open(src_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {str(e)}")

    with open(dst_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
