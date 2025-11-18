# ЛР6 — CLI‑утилиты с argparse (cat/grep‑lite + конвертеры): Техническое задание

# cli_text.py
```python
import argparse , sys , os

def cat_command(input_file: str, number_lines: bool = False):
    if not os.path.exists(input_file):
        print(f"Ошибка: файл '{input_file}' не найден", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as file:
            for i, line in enumerate(file, 1):
                if number_lines:
                    print(f"    {i} {line}", end='')
                else:
                    print(line, end='')
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}", file=sys.stderr)
        sys.exit(1)

def stats_command(input_file: str, top_n: int = 5):
    if not os.path.exists(input_file):
        print(f"Ошибка: файл '{input_file}' не найден", file=sys.stderr)
        sys.exit(1)
    
    if top_n <= 0:
        print("Ошибка: --top должен быть положительным числом", file=sys.stderr)
        sys.exit(1)
    
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as file:
            text = file.read()
            
        words = text.lower().split()
        cleaned_words = [word.strip('.,!?;:()[]{}"\'') for word in words if word.strip('.,!?;:()[]{}"\'')]
        
        word_count = {}
        for word in cleaned_words:
            word_count[word] = word_count.get(word, 0) + 1
        
        print(f"Всего слов: {sum(word_count.values())}")
        print(f"Уникальных слов: {len(word_count)}")
        print(f"Топ-{top_n}:")
        print("слово     | частота")
        print("---")
        
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        max_word_length = max(len(word) for word, _ in sorted_words[:top_n])
        
        for word, count in sorted_words[:top_n]:
            print(f"{word:<{max_word_length}} | {count}")
                
    except Exception as e:
        print(f"Ошибка при анализе файла: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для работы с текстом")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    
    stats_parser = subparsers.add_parser("stats", help="Анализ частот слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)
    
    args = parser.parse_args()
    
    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
if __name__ == "__main__":
    main()
```
## Вывод строк с номерами:
<img width="649" height="53" alt="image" src="https://github.com/user-attachments/assets/2aeca97e-abd7-4991-bc1e-47dd5bc355ab" />

## Вывод топ слов:
<img width="658" height="197" alt="image" src="https://github.com/user-attachments/assets/6838a07a-568c-486c-8437-db63d2d95499" />

# cli_convert.py
``` python
import argparse
import sys
import os
import json
import csv

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

def convert_csv_to_excel(input_file: str, output_file: str):
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        for row in data:
            f.write(','.join(row) + '\n')

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
            convert_csv_to_excel(args.source, args.target)
            print("CSV -> XLSX: Успешно")
            
    except Exception as error:
        print(f"Ошибка преобразования: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
## Вывод JSON -> CSV:
<img width="722" height="38" alt="image" src="https://github.com/user-attachments/assets/aa895381-991b-474b-adaa-d86a9a274126" />
<img width="398" height="191" alt="image" src="https://github.com/user-attachments/assets/9cf4a50a-b0cb-431e-8c91-956084c6b6da" />
<img width="331" height="183" alt="image" src="https://github.com/user-attachments/assets/3c8b1fdd-c5da-459f-8fff-0f7896e28b8e" />

## Вывод CSV -> JSON:
<img width="722" height="37" alt="image" src="https://github.com/user-attachments/assets/5825d137-9a3f-4126-810a-df5e8c82a030" />

## Вывод CSV -> XLSX:
<img width="727" height="38" alt="image" src="https://github.com/user-attachments/assets/feadb797-a8e5-43f1-92e7-90fb9c4fea47" />

## Help:
<img width="541" height="183" alt="image" src="https://github.com/user-attachments/assets/5332948a-e517-4d59-8721-ddb47f0afa44" />














