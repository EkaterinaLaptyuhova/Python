# Exercise 6-1
# print("Exercise 6-1")

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    total = x + y + z
    square = b(total) ** 2
    return square


x = 1
y = x + 1
# print(c(x, y + 3, x + y))
# print('\n')


# Exercise 6-2
print("Exercise 6-2")


def ack(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        while m > 0 and n > 0:
            a = ack(m, n-1)
            return ack(m - 1, a)


print(ack(3, 4))
