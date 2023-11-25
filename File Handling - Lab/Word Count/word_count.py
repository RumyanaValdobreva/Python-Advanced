with open("words.txt", "r") as f:
    searched_words = f.read().split()

with open("input.txt", "r") as f:
    text = f.read().lower()

words = {}

for searched_word in searched_words:
    words[searched_word] = text.count(searched_word)


with open("output.txt", "w") as f:
    for key, value in sorted(words.items(), key=lambda x: -x[1]):
        f.write(f"{key} - {value}\n")

