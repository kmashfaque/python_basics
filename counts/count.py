from collections import Counter


with open("py\counts\data.txt")as file:
    letter_counts = Counter()

    for letters in file:
        line_letters = [char for char in letters.lower() if char.isalpha()]
        letter_counts.update(line_letters)

for letter, count in letter_counts.most_common()[:-2:-1]:
    print(letter, ">>", count)
