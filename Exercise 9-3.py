fin = open('D:/words.txt')


"""
print("Exercise 9-3")


def avoid(avoid_symbols):
    count_of_words = 0
    for line in fin:
        word = line.strip()
        i = 0
        while i < len(avoid_symbols):
            if avoid_symbols[i] not in word:
                i = i +1
            else:
                break
        if i == len(avoid_symbols):
            print(word)
            count_of_words = count_of_words + 1
    print("Count of words without avoid symbols is: ", count_of_words)

characters = input("Write avoid symbols: ")
avoid(characters)



print("Exercise 9-5")


def uses_all(possible_symboles):
    for line in fin:
        word = line.strip()
        i = 0
        while i < len(possible_symboles):
            if possible_symboles[i] in word:
                i = i + 1
            else:
                break
        if i == len(possible_symboles) and i == len(word):
            print(word)


possible = input("Write possible symbols: ")
uses_all(possible)
"""

print("Exercise 9-6")

# можно оформить в виде функции с входными данными в виде
def is_abc(text):
    for line in fin:
        word = line.strip()
        i = 0
        while i < len(word) - 1:
            if word[i] <= word[i+1]:
                i = i + 1
            else:
                break
        if i == len(word) - 1:
            print(word)


is_abc(fin)
