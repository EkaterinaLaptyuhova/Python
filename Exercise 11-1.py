
def in_file(open_file):
    words = dict()
    for line in open_file:
        word = line.strip()
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

    for key in sorted(words):
        print(key, words[key])

    in_str = input("Please, write a word: ")

    if in_str in words:
        print("We have this word")
    else:
        print("We don't")


in_file(open('D:/words1.txt'))

