def findLargest(a,b,c):
    if(a > b and a > c):
        print(a, "is greater")
    elif(b > a and b > c):
        print(b , "is greater")
    else:
        print(c, "is greater")

num1  = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))
num3 = int(input("enter 3rd number : "))
findLargest(num1,num2,num3)