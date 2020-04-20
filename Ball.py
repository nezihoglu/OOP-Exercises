class Ball:
    def __init__(self, x, y, radius, xDelta, yDelta):
        self.x = x
        self.y = y
        self.radius = radius
        self.xDelta = xDelta
        self.yDelta = yDelta

    def __str__(self):
        return "Ball[(" + str(self.x) + "," + str(self.y) + "), speed(" +\
               str(self.xDelta) + "," + str(self.yDelta) + ")]"

    def getX(self):
        return self.x

    def setX(slef, newX):
        self.x = newX

    def getY(self):
        return self.y

    def setY(slef, newY):
        self.y = newY

    def getRadius(self):
        return self.radius

    def setRadius(self, newRadius):
        self.radius = newRadius

    def getXDelta(self):
        return self.xDelta

    def setXDelta(self, newXDelta):
        self.xDelta = newXDelta

    def getYDelta(self):
        return self.yDelta

    def setYDelta(self, newYDelta):
        self.yDelta = newYDelta

    def move(self):
        self.x += self.xDelta
        self.y += self.yDelta

    def reflectHorizontal(self):
        self.xDelta -= self.xDelta

    def reflectVertical(self):
        self.yDelta -= self.yDelta

    

ball = Ball(0.5, 0.5, 1, 1.5, 1.5)
print(ball)
ball.move()
print(ball)
