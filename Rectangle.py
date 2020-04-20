class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def setLength(self, newLength):
        self.length = newLength

    def setWidth(self, newWidth):
        self.width = newWidth

    def __str__(self):
        return "{width = " + str(self.width) +\
               ", length="  + str(self.length) + "}"

    def getArea(self):
        return self.width * self.length

    def getPerimeter(self):
        return self.width * 2 + self.length * 2

dikdortgen1 = Rectangle()
dikdortgen2 = Rectangle(5.0, 3.0)

print(dikdortgen1.getLength())
print(dikdortgen1.getWidth())

print(dikdortgen2.getLength())
print(dikdortgen2.getWidth())

dikdortgen1.setLength(3)
dikdortgen1.setWidth(1.5)

print(dikdortgen1.getLength())
print(dikdortgen1.getWidth())

print(dikdortgen1)
print(dikdortgen2)

print(dikdortgen1.getArea())
print(dikdortgen1.getPerimeter())






