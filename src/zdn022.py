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
    create_directory(r"C:\Users\eniko\PycharmProjects\PythonProject\data")

    output_path = os.path.join(output_dir, "report.csv")
    with open(output_path, "w", encoding="cp65001", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(sorted_words)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    print(table(top_n(freqs, 5), True))
