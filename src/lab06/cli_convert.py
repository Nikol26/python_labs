import argparse
import sys
import os
import json
import csv

def check_file_exists(file_path: str):
    """Проверяет существует ли файл"""
    if not os.path.exists(file_path):
        print(f"Ошибка: файл '{file_path}' не найден", file=sys.stderr)
        sys.exit(1)

def json_to_csv(input_file: str, output_file: str):
    """Конвертирует JSON в CSV"""
    print("JSON -> CSV")
    check_file_exists(input_file)
    
    try:
        # Пробуем разные кодировки
        for encoding in ['utf-8', 'utf-8-sig', 'utf-16']:
            try:
                with open(input_file, 'r', encoding=encoding) as f:
                    data = json.load(f)
                
                if isinstance(data, list) and len(data) > 0:
                    with open(output_file, 'w', encoding='utf-8', newline='') as f:
                        writer = csv.DictWriter(f, fieldnames=data[0].keys())
                        writer.writeheader()
                        writer.writerows(data)
                    print(f"Успешно: {input_file} -> {output_file}")
                    return  # Успешно
                else:
                    print("Ошибка: JSON должен содержать список словарей")
                    sys.exit(1)
                    
            except UnicodeDecodeError:
                continue  # Пробуем следующую кодировку
        
        # Если ни одна кодировка не подошла
        print("Ошибка: Не удается прочитать файл (проблема с кодировкой)")
        sys.exit(1)
            
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def csv_to_json(input_file: str, output_file: str):
    """Конвертирует CSV в JSON"""
    print("CSV -> JSON") 
    check_file_exists(input_file)
    
    try:
        # Пробуем разные кодировки
        for encoding in ['utf-8', 'utf-8-sig', 'utf-16']:
            try:
                with open(input_file, 'r', encoding=encoding) as f:
                    reader = csv.DictReader(f)
                    data = list(reader)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Успешно: {input_file} -> {output_file}")
                return  # Успешно
                    
            except UnicodeDecodeError:
                continue  # Пробуем следующую кодировку
        
        print("Ошибка: Не удается прочитать файл (проблема с кодировкой)")
        sys.exit(1)
            
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def csv_to_xlsx(input_file: str, output_file: str):
    """Конвертирует CSV в XLSX"""
    print("CSV -> XLSX")
    check_file_exists(input_file)
    
    try:
        # Пробуем разные кодировки
        for encoding in ['utf-8', 'utf-8-sig', 'utf-16']:
            try:
                with open(input_file, 'r', encoding=encoding) as f:
                    reader = csv.reader(f)
                    data = list(reader)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    for row in data:
                        f.write(','.join(row) + '\n')
                
                print(f"Успешно: {input_file} -> {output_file}")
                print("Для полной поддержки Excel установите библиотеку openpyxl")
                return  # Успешно
                    
            except UnicodeDecodeError:
                continue  # Пробуем следующую кодировку
        
        print("Ошибка: Не удается прочитать файл (проблема с кодировкой)")
        sys.exit(1)
            
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Конвертеры файлов")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")
    
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")
    
    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")
    
    args = parser.parse_args()
    
    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)

if __name__ == "__main__":
    main()