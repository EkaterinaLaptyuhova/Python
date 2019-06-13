def is_anagram(words):
    d = dict()
    for word in words:
        w = "".join(sorted(word))
        if w not in d:
            d[w] = [word]
        else:
            d[word].append(w)
    for key in d:
        print(d[key])


is_anagram(['ata', "dd", 'aat', 'bb'])