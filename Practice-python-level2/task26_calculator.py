def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def division(a,b):
    print(a/b)

first_num = int(input("Enter first number : "))
second_num = int(input("Enter second num : "))
operator = input("choose operation(+,-,*,/)")

if operator == "+":
    add(first_num ,second_num)
elif operator == "-":
    subtract(first_num , second_num)
elif operator == "*":
    multiply(first_num , second_num)
elif operator == "/":
    division(first_num , second_num)
else:
    print("Invalid operator !")