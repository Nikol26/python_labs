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