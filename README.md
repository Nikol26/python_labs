# ЛР3 — Тексты и частоты слов (словарь/множество)

# Задание A — src/lib/text.py
## normalize
<pre><code>
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text
print(normalize("ПрИвЕт\nМИр\t")) 
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
</code></pre>
<img width="515" height="308" alt="image" src="https://github.com/user-attachments/assets/0d863029-b948-4795-acee-6bdbd9582911" />

## tokenize 
<pre><code>
import re 
def tokenize(text: str) -> list[str]:
    return re.findall(r'[a-zA-Zа-яА-ЯёЁ]+', text)
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
</code></pre>
<img width="400" height="296" alt="image" src="https://github.com/user-attachments/assets/dd3b56d6-7c82-4260-b2b5-b8414b0d4e79" />

## count_freq + top_n
<pre><code>
def count_freq(tokens: list[str]) -> dict[str, int]:
    counts = {}  
    for word in tokens:
        current_count = counts.get(word, 0)
        counts[word] = current_count + 1
    return counts
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    temp_list = []
    for word, count in freq.items():
        temp_list.append((-count, word))
    temp_list.sort()
    result = []
    for neg_count, word in temp_list:
        result.append((word, -neg_count))

    return result[:n]
tokens_example = ["a", "b", "a", "c", "b", "a"]
freq_example = count_freq(tokens_example)
print(top_n(freq_example, n=2))
tokens_example_2 = ["bb", "aa", "bb", "aa", "cc"]
freq_example_2 = count_freq(tokens_example_2)
print(top_n(freq_example_2, n=2))
</code></pre>
<img width="490" height="435" alt="image" src="https://github.com/user-attachments/assets/1e2fb9e0-67c7-4fbd-87d6-cb66db251c8b" />

# Задание B — src/text_stats.py (скрипт со stdin)
<pre><code>
import sys
sys.path.append(r'C:\Users\VektorVkusoff\.vscode\python_labs\src')

from text import normalize, tokenize, count_freq, top_n

def table(arr: list[tuple[str, int]], isTable: bool = True) -> str:
    if not arr:
        return "(нет данных)"
    s = str()
    if isTable:
        word_col_width = max(len("слово"), max(len(a[0]) for a in arr))
        freq_col_width = max(len("частота"), max(len(str(a[1])) for a in arr))
        s += f"{'слово'.ljust(word_col_width)} | {'частота'.rjust(freq_col_width)}"
        s += "\n" + "-" * word_col_width + "-+-" + "-" * freq_col_width
        for word, freq in arr:
            s += f"\n{word.ljust(word_col_width)} | {str(freq).rjust(freq_col_width)}"
        return s
    else:
        return "\n".join(f"{a[0]}: {a[1]}" for a in arr)
def main(text: str):
    text = text.strip()
    tokens = normalize(text)
    tokens = tokenize(tokens)
    freqs = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freqs)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    top5 = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Топ-5:")
    print(table(top5, True))
</code></pre>
<img width="569" height="460" alt="image" src="https://github.com/user-attachments/assets/8edfb127-8cc7-42b3-8bec-90574d9ec22e" />

    
    




  


  

  
