import argparse
import sys
import os
import json
import csv
import os, csv, sys

from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not os.path.exists(csv_path):
        print("FileNotFoundError")
        sys.exit(1)

    if os.path.getsize(csv_path) == 0:
        print("ValueError")
        sys.exit(1)
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            ws.append(row)


    for column_cells in ws.columns:
        max_length = 0
        column_letter = column_cells[0].column_letter
        for cell in column_cells:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8)
    wb.save(xlsx_path)



def file_exists(file_path: str):
    return os.path.exists(file_path)

def convert_json_to_csv(input_file: str, output_file: str):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def convert_csv_to_json(input_file: str, output_file: str):
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Конвертер форматов файлов")
    subparsers = parser.add_subparsers(dest="action", required=True)
    
    # JSON to CSV
    json_csv = subparsers.add_parser("json2csv")
    json_csv.add_argument("--in", dest="source", required=True)
    json_csv.add_argument("--out", dest="target", required=True)
    
    # CSV to JSON
    csv_json = subparsers.add_parser("csv2json")
    csv_json.add_argument("--in", dest="source", required=True)
    csv_json.add_argument("--out", dest="target", required=True)
    
    # CSV to XLSX
    csv_excel = subparsers.add_parser("csv2xlsx")
    csv_excel.add_argument("--in", dest="source", required=True)
    csv_excel.add_argument("--out", dest="target", required=True)

    
    args = parser.parse_args()
    
    if not file_exists(args.source):
        print(f"Ошибка: Файл {args.source} не найден")
        sys.exit(1)
    
    try:
        if args.action == "json2csv":
            convert_json_to_csv(args.source, args.target)
            print("JSON -> CSV: Успешно")
            
        elif args.action == "csv2json":
            convert_csv_to_json(args.source, args.target)
            print("CSV -> JSON: Успешно")
            
        elif args.action == "csv2xlsx":
            csv_to_xlsx(args.source, args.target)
            print("CSV -> XLSX: Успешно")
            
    except Exception as error:
        print(f"Ошибка преобразования: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()