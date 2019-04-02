import turtle


bob = turtle.Turtle()
print(bob)
bob.speed(1)


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


square(bob)

def second_square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


second_square(bob, 120)