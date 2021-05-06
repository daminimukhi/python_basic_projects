import math #module

#operations in a scientific calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def sqrt(a):
    result = math.sqrt(a)
    return result

def exp(a):
    return a ** 2

def sin(x):
    result = math.sin(x)
    return result

def cos(x):
    result = math.cos(x)
    return result

def tan(x):
    result = math.tan(x)
    return result

#choosing the operation
print("""choose a number for the following operations
1- Addition(x, y)
2- Subtraction(x,y)
3- Multiplication(x,y)
4- Division(x,y)
5- Square(x)
6- Square root(x)
7- Sin(x)
8- Cos(x)
9- tan(x) """)
op = int(input('what operation do you want to perform ? '))

#calculator Script
while op < 10:
    if op == 1:
        print("Enter the paratmeters")
        x1 = int(input("Enter x"))
        y1 = int(input("Enter y"))
        res1 = add(x1, y1)
        print("Additon = ", res1)
    elif op == 2:
        x2 = int(input("Enter x"))
        y2 = int(input("Enter y"))
        res2 = subtract(x2, y2)
        print("Subtraction = ", res2)
    elif op == 3:
        x3 = int(input("Enter x"))
        y3 = int(input("Enter y"))
        res3 = multiply(x3, y3)
        print("Multiplication =", res3)
    elif op == 4:
        x4 = int(input("Enter x"))
        y4 = int(input("Enter y"))
        res4 = divide(x4, y4)
        print("division = ", res4)
    elif op == 5:
        x5 = int(input("Enter x"))
        res5 = exp(x5)
        print("Square =", res5)
    elif op == 6:
        x6 = int(input("Enter x"))
        res6 = sqrt(x6)
        print("Square_root =", res6)
    elif op == 7:
        x7 = int(input("Enter x"))
        res7 = sin(x7)
        print("Sin(x) = ", res7)
    elif op == 8:
        x8 = int(input("Enter x"))
        res7 = cos(x8)
        print("Cos(x) = ", res8)
    elif op == 9:
        x9 = int(input("Enter x"))
        res8 = tan(x9)
        print("Tan(x) = ", res9)

    else:
        print('Choose another operation ')

    new = int(input("do you want to continue - (Yes - 1), (No - 0)"))
    if new == 1:
        op = int(input("Enter operation"))
    elif new == 0:
        print("Thanks for using this Calculator")
        break