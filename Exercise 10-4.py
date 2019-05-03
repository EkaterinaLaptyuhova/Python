def is_anagram(s1, s2):
    i = 0
    if len(s1) < len(s2) or len(s1) > len(s2):
        print("False")
    else:
        t1 = list(s1)
        t2 = list(s2)
        while i < len(t1):
            if t1[i] == t2[0]:
                del t1[i]
                del t2[0]
                i = 0
            else:
                i += 1

        if t2 == []:
            print("True")
        else:
            print("False")


is_anagram('katya', 'akaty')