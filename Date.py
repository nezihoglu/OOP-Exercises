class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "Date[" + str(self.day) + "/ " + \
               str(self.month) + "/ " + str(self.year) + "]"

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def setDay(self, newDay):
        self.day = newDay

    def setMonth(self, newMonth):
        self.month = newMonth

    def setYear(self, newYear):
        self.year = newYear

    def setDate(self):
        self.Date = newDate

tarih1 = Date(20, 4, 2020)
tarih2 = Date(21, 'April', 2020)

print(tarih1)
print(tarih2)

