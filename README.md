# Лабораторная работа №5

## Задание А - JSON ↔ CSV
```python
import csv, json, sys, os
from pathlib import Path 

def right_json(path: str)-> bool:
    path=Path(path)
    if path.suffix.lower() != ".json":
        return False

def right_csv(path: str)-> bool:
    path=Path(path)
    if path.suffix.lower() != ".csv":
        return False


def is_valid_json_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
        
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return isinstance(json_data, list) and len(json_data) > 0 and all(isinstance(item, dict) for item in json_data) #все элементы в списке являются словарями
    except:
        return False

def is_valid_csv_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            return False
            
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)  # Создаем объект reader для чтения CSV файла построчно
            header = next(reader, None) # Читаем первую строку (заголовок) из CSV файла
            return header is not None and len(header) > 0
    except:
        return False

def json_to_csv(json_path: str, csv_path: str) -> None:
    if not is_valid_json_file(json_path): # Проверяем валидность CSV файла с помощью нашей функции
        print("ValueError: Input file is not a valid JSON or is empty")
        sys.exit(1) # Завершаем программу с кодом ошибки 1
    if not right_json(json_path):
        print("ValueError: неверный формат файла")
    if not right_csv(csv_path):
        print("ValueError: неверный формат файла")
    

    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file) # Загружаем и парсим JSON данные в переменную json_data

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys()) # Создаем объект DictWriter для записи словарей в CSV
        writer.writeheader()  # Записываем заголовок в CSV файл
        writer.writerows(json_data) # Записываем все данные из json_data в CSV файл построчно

def csv_to_json(csv_path: str, json_path: str) -> None:
    if not is_valid_csv_file(csv_path):
        print("ValueError: Input file is not a valid CSV or is empty")
        sys.exit(1)
    if not right_json(json_path):
        print("ValueError: неверный формат файла")
    if not right_csv(csv_path):
        print("ValueError: неверный формат файла")

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Создаем объект DictReader для чтения CSV в виде словарей
        data = list(reader) # Читаем все строки и преобразуем в список словарей
    
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4) #разрешаем Unicode символы м красиво форматирум с отпступом 4 пробела
csv_to_json(r'C:\Users\VektorVkusoff\.vscode\python_labs\src\people.csv', r'C:\Users\VektorVkusoff\.vscode\python_labs\src\people_from_csv.json')

json_to_csv(r'C:\Users\VektorVkusoff\.vscode\python_labs\src\people.json', r'C:\Users\VektorVkusoff\.vscode\python_labs\src\people_from_json.csv')
```  
<img width="270" height="124" alt="image" src="https://github.com/user-attachments/assets/4d8aaadf-1375-4bfe-88fe-8d07b74e1a12" />
<img width="279" height="143" alt="image" src="https://github.com/user-attachments/assets/312eb193-a4f1-4357-acb2-01be5b0f627c" />
<img width="348" height="143" alt="image" src="https://github.com/user-attachments/assets/5d7733ee-0e02-4ce3-bbaf-b94af7692651" />
<img width="245" height="98" alt="image" src="https://github.com/user-attachments/assets/0fbb3b69-8e7c-4572-b2b3-823cbee14c7a" />  

## Задание B — CSV → XLSX
```python
from pathlib import Path
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    csv_path = Path (csv_path)
    xlsx_path = Path(xlsx_path)
    
    # Проверка
    if not csv_path.exists():
        raise FileNotFoundError('Файл не найден')
    if csv_path.suffix.lower() != '.csv':
        raise ValueError('Неверный тип файла')
    try:
        with open (csv_path, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)
    except UnicodeDecodeError:
        raise ValueError ('Ошибка кодировки')
    except csv.Error:
        raise ValueError ('Ошибка формата CVS')
    if not data:
        raise ValueError ('Файл пуcтой, ожидаются данные')
    
    # Создание excel файла
    work_book = Workbook()
    work_sheet = work_book.active
    work_sheet.title = "Sheet_Nikol"
    
    # Чтение csv и запись в excel
    with csv_path.open(encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            work_sheet.append(row)
    
    work_book.save(xlsx_path)
    return "Выполнено успешно"

print (csv_to_xlsx('src/people.csv', 'src/people.xlsx'))
```
<img width="359" height="139" alt="image" src="https://github.com/user-attachments/assets/19383f7d-8b0e-4bd4-94c5-8685af359c2e" />
<img width="284" height="129" alt="image" src="https://github.com/user-attachments/assets/f0881f8b-7d1a-41ef-99c7-2cd0ceeb846e" />










