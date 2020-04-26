class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "Time[" + str(self.hour) + ":" + \
               str(self.minute) + ":" + str(self.second) + "]"

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setHour(self, newHour):
        self.hour = newHour

    def setMinute(self, newMinute):
        self.minute = newMinute

    def setSecond(self, newSecond):
        self.second = newSecond

    def setTime(self):
        self.Time = newTime

    def nextSecond(self):
        self.second += 1

    def previousSecond(self):
        self.second -= 1

vakit1 = Time(0, 0, 0)
vakit2 = Time(22, 35, 57)

print(vakit1)
print(vakit2)
vakit2.nextSecond()
print(vakit2)
vakit2.previousSecond()
print(vakit2)
