# !/usr/bin/python3
# Filename: project1.py
# this code is about class and object in python which shows various class attributes in python how to access them and use them in python without any entry  of data from user
#  class and object in python
class employee:
    empCount  = 0
    def __init__(self, name, salary):
        self.name  =  name
        self.slary  = salary
        employee.empCount+=1
    def displayCount(self):
        print("toal number of employee %d" % employee.empCount)
    def displayEmployee(self):
        print("name: ", self.name ,", salary: ", self.salary)

print("Employe__doc__: ", employee.__doc__)
print("Employee__name__: ", employee.__name__)
print("Employee__module__: ", employee.__module__)
print("Employee__bases__: ", employee.__bases__)
print("Employee__dict__: ", employee.__dict__)
