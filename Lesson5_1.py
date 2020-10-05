# написать программу, в которой на входе список чисел,
# а на выходе мы выдаем список чисел, которые повторяются более одного раза

first_l = [34, 4, 5, 1, 34, 5, 5, 5, 6, 1]
first_l.sort()
second_l = []
for i in range(len(first_l) - 1):
    if (first_l[i] == first_l[i + 1]) and (first_l[i] not in second_l):
        second_l.append(first_l[i])

print(second_l)

