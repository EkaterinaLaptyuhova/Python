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
            while word[i] == word[i+1]:
                i = i + 1
                return i
            k = i
            while word[k] != word[k+1]:
                k = k + 1
                return k
            if i + 1 == k:
                count = count + 1
            else:
                count = 0
            if count == 3:
                print(word)


new_fun(fin)
