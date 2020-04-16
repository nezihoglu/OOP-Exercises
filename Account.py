class Account:
    def __init__(self, id, Name, Surname, balance):
        self.id = id
        self.Name = Name
        self.Surname = Surname
        self.balance = balance

    def __str__(self):
        return "Account[" + "ID: " + str(self.id) + ", " + \
               "Name: " + self.Name + ", " + "Surname: " + self.Surname + \
               ", " + "Balance: " + str(self.balance) + "]"

    def getID(self):
        return self.id

    def getName(self):
        return self.Name

    def getSurname(self):
        return self.Surname

    def getBalance(self):
        return self.balance

    def getFullname(self):
        return self.Name + " " + self.Surname

    def getCredit(self, amount):
        self.amount = amount
        if self.amount <= self.balance:
            self.balance = self.balance - self.amount
        else:
            print("amount exceeded")
        return self.balance

halim = Account(123, 'Halim', 'Nezihoglu', 100)
print(halim)

print(halim.getID())
print(halim.getFullname())
print(halim.getBalance())
print(halim.getCredit(20))

print(halim)
