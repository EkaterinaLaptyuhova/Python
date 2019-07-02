from math import sqrt


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def point(self, x, y):
        self.x = x
        self.y = y

    def representation(self):
        print("Circle with the radius ", str(self.radius),  " and the centre is ", str(self.x), ", ", str(self.y))

    def point_in_circle(self, x1, y1):
        distance = sqrt(((self.x - x1) ** 2) + (self.y - y1) ** 2)
        if distance <= self.radius:
            return True
        else:
            return False


first_circle = Circle(75)

first_circle.point(150, 100)
first_circle.representation()
print(first_circle.point_in_circle(160, 100))