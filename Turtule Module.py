import turtle


bob = turtle.Turtle()
print(bob)
bob.speed(0)


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
    bob.reset()

# square(bob)

def second_square(t, length):
    bob.speed(1)
    for i in range(4):
        t.fd(length)
        t.lt(90)
    bob.reset()


# second_square(bob, 120)


def polygon(t, n, length):
    bob.speed(1)
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    bob.reset()


# polygon(bob, n = 30, length = 3)


# t = bob, n - kol-vo list'ev, length - dlina lista po pryamoi
bob.reset()
def first_flower(t, n, length):
    bob.speed(0)
    for repeat in range(n):
        for i in range(length):
            t.lt(1)
            t.fd(1)
        t.lt(180 - length)
        for k in range(length):
            t.lt(1)
            t.fd(1)
        t.rt(180 - int(360/n) + length)


first_flower(bob, 18, 90)
