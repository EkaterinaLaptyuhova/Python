fin = open('D:/words1.txt')

"""
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
                if word[i] == word[i-1]:
                    i += 1
            else:
                i = i + 1
                k = 0


fun(fin)
"""

def new_fun(text):
    for line in fin:
        word = line.strip()
        i = 0
        count = 0
        while i < len(word) - 1:
            while i < len(word) - 1 and word[i] == word[i + 1]:
                i = i + 1
            k = i
            count = count + 1
            while k < len(word) - 1 and word[k] != word[k + 1]:
                k = k + 1
            if i + 1 != k:
                count = 0
                i = k
            if count == 3:
                print(word)
                break


new_fun(fin)
