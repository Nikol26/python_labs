import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic(tmp_path):
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"

    test_data = [{"name": "Анна", "age": 25}, {"name": "Борис", "age": 30}]

    src.write_text(json.dumps(test_data, ensure_ascii=False), encoding="utf-8")
    json_to_csv(str(src), str(dst))
    assert dst.exists()


def test_csv_to_json_basic(tmp_path):
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.json"

    csv_content = "name,age\nАнна,25\nБорис,30"
    src.write_text(csv_content, encoding="utf-8")
    csv_to_json(str(src), str(dst))
    assert dst.exists()
