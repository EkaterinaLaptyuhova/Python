def is_anagram(s1, s2):

    if len(s1) != len(s2):
        print('False')
        return False

    i = 0
    k = 0
    while i <= len(s1) - 1:
        while k <= len(s2) - 1:
            if s2[k] == s1[i]:
                s2 = s2[ : k] + s2[k+1 : ]
                k = len(s2)
            else:
                k += 1

        if len(s2) != len(s1) - (i + 1):
            print('False')
            return False
        else:
            k = 0
            i += 1

    print("True")


is_anagram('katya', 'katya')

