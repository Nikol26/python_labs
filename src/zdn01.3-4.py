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