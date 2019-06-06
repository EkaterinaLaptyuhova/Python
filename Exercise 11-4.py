def has_duplicates(list_of_words):
    dict_words = dict()
    for element in list_of_words:
        if element not in dict_words:
            dict_words[element] = 1
        else:
            print("True")
            return True
    print("False")
    return False


has_duplicates(['aa', 'a', 'dd', 's', 's', 's'])