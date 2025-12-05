class employee:
    def __init__(self,name,salary):
        self.name  = name
        self.salary =  salary
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
class salesofficer(employee):
    def __init__(self,name,salary,inc):
        super().__init__(name,salary)
        self.incnt = inc
    def getsalary(self):
        return self.salary + self.incnt
    

e1=employee("Rajesh", 9000)
print ("Total salary for {} is Rs {}".format(e1.getname(),e1.getsalary()))
s1=salesofficer('Kiran', 10000, 1000)
print ("Total salary for {} is Rs {}".format(s1.getname(),s1.getsalary()))