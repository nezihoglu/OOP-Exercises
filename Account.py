class Account:
    def __init__(self, id, name, balance = 0):
        self.id = id
        self.name = name
        if balance >= 0:
            self.balance = balance

    def __str__(self):
        return "Account[" + \
               "id=" + str(self.id) + "," + \
               "name=" +self.name + "," + \
               "balance=" + str(self.balance) + \
               "]"

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def credit(self, amount):
        if amount >= 0:
            self.balance += amount

        return self.balance

    def debit(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
        else:
            print("amount exceeded")

        return self.balance

    def transferTo(self, another, amount):
        if self.balance >= amount:
            self.balance -= amount
            another.credit(amount)
        else:
            print("amount exceeded")

        return self.balance

hesap1 = Account(1, 'Halim')
hesap2 = Account(2, "Nurlan", 1000)

print("Yeni balance")
print(hesap1.credit(500))
print(("Kestikten sonraki balance"))
print(hesap1.debit(300))
print("Transfer islemden sonra kalan miktar")
print(hesap1.transferTo(hesap2, 100))
print("Transfer islemden sonra kalan miktar")
print(hesap2.transferTo(hesap1, 300))
