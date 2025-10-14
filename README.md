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



  


  

  
