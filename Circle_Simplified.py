import math

class Circle_Simplified:
    def __init__(self, radius = 1.0):
        self.radius = radius

    def __str__(self):
        return "Circle[" + "radius=" + str(self.radius) + "]"

    def getRadius(self):
        return self.radius

    def setRadius(self, newRadius):
        self.radius = newRadius

    def getArea(self):
        return math.pi * self.radius * self.radius

    def getCircumference(self):
        return 2 * math.pi * self.radius

circle1 = Circle_Simplified()
circle2 = Circle_Simplified(1.5)

print(circle1)
print(circle2)

print(circle1.getArea())
print(circle1.getCircumference())
print(circle2.getArea())
print(circle2.getCircumference())
