# Exercise 5-1
import time


print("Exercise 5-1")
current_time = time.time()
print(current_time)
days = int(current_time // 86400)
years = int(days // 365)
sec_current_day = int(current_time % 86400)
hours = int(sec_current_day // 3600)
min = (sec_current_day - int(hours * 3600)) // 60
sec = int(sec_current_day - ((sec_current_day - int(hours * 3600)) // 60) * 60 - int(hours * 3600))
print(hours, ":", min, ".", sec)
print('\n')


# Exercise 5-2
print("Exercise 5-2")


def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


data_a = int(input("Check Fermat theorem! Please, write variables a = "))
data_b = int(input("Check Fermat theorem! Please, write variables b = "))
data_c = int(input("Check Fermat theorem! Please, write variables c = "))
data_n = int(input("Check Fermat theorem! Please, write variables n = "))
check_fermat(data_a, data_b, data_c, data_n)
print("/n")



# Exercise 5-3
print("Exercise 5-3")


def is_triangle(a, b, c):
    if (a + b >= c) or (a + c >= b) or (b + c >= a):
        print("It is a triangle!")
    else:
        print("It isn't a triangle!")


side_a = int(input("Please, write the first side = "))
side_b = int(input("Please, write the second side = "))
side_c = int(input("Please, write the third side = "))
is_triangle(side_a, side_b, side_c)
print("/n")





