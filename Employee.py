class Employee:
    def __init__(self, id, firstName, lastName, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def __str__(self):
        return "Employee[" + \
               "id= " + str(self.id) + ", " + \
               "name= " + self.firstName + ", " + " lastname= " + \
               self.lastName + ", " + "salary= " + str(self.salary) + "]"

    def getID(self):
        return self.id

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getName(self):
        return self.firstName + " " + self.lastName

    def getSalary(self):
        return self.salary

    def setSalary(self, newSalary):
        self.salary = newSalary

    def getAnnualSalary(self):
        return self.salary * 12

    def raiseSalary(self, percent):
        self.salary = self.salary + self.salary * (percent/100.0)


halim = Employee(11, "Halim", "Nezihoglu", 100.0)

print(halim)

print(halim.getID())
print(halim.getFirstName())
print(halim.getLastName())
print(halim.getSalary())
print(halim.getName())

halim.setSalary(100.0)
print(halim.getAnnualSalary())

halim.raiseSalary(5)

print(halim)























    
