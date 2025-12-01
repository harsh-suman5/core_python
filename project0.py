#  class and object in python
class employee:
    empCount = 0
    def __init__(self, name,salary):
        self.name  = name
        self.salary  = salary
        employee.empCount+=1
    def displayCount(self):
        print("total employee %d" % employee.empCount)
    def displayEmployee(self):
        print("name: ",self.name,", salary: " ,self.salary)
emp1  = employee("harsh",  "50000")
emp2  = employee("priti", 40000)
emp1.displayEmployee()
emp2.displayEmployee()
print("total employee %d" % employee.empCount)
emp1.age =  23
emp2.age  = 20
del emp1.age

del emp2.age




