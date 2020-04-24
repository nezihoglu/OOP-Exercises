class InvoiceItem:
    def __init__(self, id, desc, qty, unitPrice):
        self.id = id
        self.desc = desc
        self.qty = qty
        self.unitPrice = unitPrice

    def __str__(self):
        return "InvoiceItem[" + "id= " + self.id + ", " + \
               "description= " + self.desc + ", " + \
               "quantity= " + str(self.qty) + "kg, " + \
               "unitPrice= " + str(self.unitPrice) + "som" + "]"

    def getId(self):
        return self.id

    def getDesc(self):
        return self.desc

    def getQty(self):
        return self.qty

    def setQty(self, newQty):
        self.qty = newQty

    def getUnitPrice(self):
        return self.unitPrice

    def setUnitPrice(self, newUnitPrice):
        self.unitPrice = newUnitPrice

    def getTotal(self):
        return self.unitPrice * self.qty
    

fatura = InvoiceItem('Halim', 'un', 10, 40.0)

print(fatura)

print(fatura.getId())
print(fatura.getDesc())
print(fatura.getQty())
print(fatura.getUnitPrice())
print(fatura.getTotal())

fatura.setUnitPrice(50.0)
print(fatura.getTotal())
