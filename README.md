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
<img width="632" height="55" alt="image" src="https://github.com/user-attachments/assets/4e80f7ff-c8df-4a59-8e9f-44382566a86d" />

## Вывод топ слов:
<img width="623" height="187" alt="image" src="https://github.com/user-attachments/assets/4d4dbc48-5686-436f-9da0-991d1e37226b" />



