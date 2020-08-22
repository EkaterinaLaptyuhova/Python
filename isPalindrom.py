cutted = ""
palindrom = str(input("vvedite stroky: "))
for i in palindrom:
    if i != " ":
        cutted += i

perevertysh = ""
ind = len(cutted)
while ind > 0:
    perevertysh += cutted[ind - 1: ind]
    ind -= 1

if perevertysh == cutted:
    print("palindrom")
else:
    print("ne palindrom")