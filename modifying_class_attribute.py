class employee:
    empCount  = 0
    def __init__(self,name,age):

        self.__name = name
        self.__age  = age
        employee.empCount+=1
        print("name: ", self.__name,",age: ",self.__age)
        print("employee count: ", employee.empCount)
e1 =  employee("harsh", 23)
print()
e2  = employee("jahanvi", 22)
