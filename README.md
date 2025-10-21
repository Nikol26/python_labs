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

## Задание B — скрипт src/lab04/text_report.py
<pre><code>
import os, csv 
from text import tokenize, top_n, normalize
from zdn02 import read_text, ensure_parent_dir
from zdn01 import count_freq
in1 = True
if in1:
    print("Режим один файл:")

    path = r"C:\Users\VektorVkusoff\OneDrive\Документы\GitHub\python_labs\data\input.txt"
    text = read_text(path)
    words = tokenize(normalize(text))
    total_words = len(words)
    freqs = count_freq(words)
    unique_words = len(freqs)
    sorted_words = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))

    output_dir = r"C:\Users\VektorVkusoff\OneDrive\Документы\GitHub\python_labs\data"
    ensure_parent_dir(r"C:\Users\VektorVkusoff\OneDrive\Документы\GitHub\python_labs\data")

    output_path = os.path.join(output_dir, "report.csv")
    with open(output_path, "w", encoding="cp65001", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(sorted_words)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for i in sorted_words:
        print(i[0],i[1])  
</code></pre>
<img width="748" height="623" alt="image" src="https://github.com/user-attachments/assets/d83debfc-86cb-4d78-9f50-ddd3b4a4bccb" />
<img width="731" height="250" alt="image" src="https://github.com/user-attachments/assets/c47cad35-25ee-4ffd-8b21-2313cf23331c" />


  





  


