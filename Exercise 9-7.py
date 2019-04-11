fin = open('D:/words1.txt')


def fun(text):
    for line in fin:
        word = line.strip()
        i = 0
        k = 0
        while i < len(word) - 1:
            if word[i] == word[i+1]:
                i = i + 2
                k = k + 1
                if k == 3:
                    print(word)
            else:
                i = i + 1
                k = 0


fun(fin)

