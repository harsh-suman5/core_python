#add attributes dynamically by using setattr() function
class employee:
    pass

    @classmethod
    def company_name(cls):
      print("welcomne to the portal of harsh academy live.")


setattr(employee, "harsh", employee.company_name)
emp1 = employee()
emp1.company_name()