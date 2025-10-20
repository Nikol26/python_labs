# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

## Задание A — модуль src/lab04/io_txt_csv.py
<pre><code>
  from pathlib import Path
import csv
import os
from typing import Iterable, Sequence
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    try:
        return Path(path).read_text(encoding=encoding)
    except FileNotFoundError:
        return "Такого файла нету"
    except UnicodeDecodeError:
        return "Неудалось изменить кодировку"
def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    with p.open('w', newline="", encoding="utf-8") as file:
        file_c = csv.writer(file)   
        if header is None and rows == []:
            file_c.writerow(('a', 'b'))
        if header is not None:
            file_c.writerow(header)
        if rows != []:
            const = len(rows[0])
            for i in rows:
                if len(i) != const:
                    return ValueError
        file_c.writerows(rows)
def ensure_parent_dir(path: str | Path) -> None:
    path = os.path.dirname(path)
    Path(path).mkdir(parents=True, exist_ok=True)
print(read_text(r"C:\Users\VektorVkusoff\OneDrive\Документы\GitHub\python_labs\data\input.txt"))
write_csv([("word","count"),("test",3)], r"C:\Users\VektorVkusoff\OneDrive\Документы\GitHub\python_labs\data\check.csv") 
</code></pre>
<img width="868" height="569" alt="image" src="https://github.com/user-attachments/assets/42543c22-0bb6-4b09-b211-18058208ee62" />
<img width="711" height="607" alt="image" src="https://github.com/user-attachments/assets/a05758c9-7485-4def-a329-2c95e291ec80" />




  


