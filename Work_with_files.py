def read_file(file):

    with open(file, "r", encoding="UTF-8") as f:
        return f.read().replace(".","").replace(",","").replace("!","") \
                .replace("?","").lower().split()


def save_file(file, words):

    with open(file, "w", encoding="UTF-8") as f:
        
        unique_words = list(set(words))
        unique_words.sort()

        f.write(f"Всего уникальныъ слов: {len(unique_words)} \n========================")
        for word in unique_words:
            f.write(f"{word}\n")

save_file("output.txt", read_file("data.txt"))