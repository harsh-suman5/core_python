num = 4
print(type(num)) # Output: <class 'int'>
num1  = 4.5
print(type(num1)) # Output: <class 'float'>
num2 = 3 + 4j
print(type(num2)) # Output: <class 'complex'>
print("real part: ", num2.real) # Output: real part: 3.0
print("imaginary part: ", num2.imag) # Output: imaginary part: 4.0
print("complex number: ", num2) # Output: complex number: (3+4j)

dct = {"name": "harsh", "age": 23}
print(type(dct)) # Output: <class 'dict'>
def sayhello():
    print ("hello world")
    return
print(type(sayhello)) # Output: <class 'function'>
