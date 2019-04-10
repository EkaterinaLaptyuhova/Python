fin = open('D:/words.txt')
# line = fin.readline()
# word = line.strip()

characters = int(input("Write count of characters: "))
i = 0
k = 0
for line in fin:
    word = line.strip()
    data = word.find('e')
    if data == -1 and len(word) > characters:
        print(word)
        i = i + 1
    k = k + 1

print(i, k)
