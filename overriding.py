class employee:
    def department(self):
        print("this is a parent class method")
class sales(employee):
    def department(self):
        print("this is a child class method")
e = employee()
e.department()
s = sales()
s.department()