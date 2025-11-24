import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_simple():
    result = normalize("ПРИВЕТ")
    assert result == "привет"


def test_normalize_empty():
    result = normalize("")
    assert result == ""


def test_tokenize_basic():
    result = tokenize("привет мир")
    assert result == ["привет", "мир"]


def test_count_freq_basic():
    result = count_freq(["яблоко", "банан", "яблоко"])
    assert result == {"яблоко": 2, "банан": 1}


def test_top_n_basic():
    freq = {"яблоко": 5, "банан": 3, "апельсин": 7}
    result = top_n(freq, 2)
    assert result == [("апельсин", 7), ("яблоко", 5)]
