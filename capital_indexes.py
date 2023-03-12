
def capital_indexes(word):
    indexes = []

    for i in range(len(word)):
        if word[i].isupper():
            indexes.append(i)

word = "HeLlO"

print(capital_indexes(word))