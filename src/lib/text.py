def normalize(text: str) -> str:
    if not text:
        return ""
    text = text.lower()
    text = text.replace("ё", "е")
    import re

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokenize(text: str) -> list[str]:
    if not text:
        return []
    import re

    words = re.findall(r"\b[а-яa-z]+\b", text, re.IGNORECASE)
    return words


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        token = token.lower()
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    if not freq:
        return []
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
