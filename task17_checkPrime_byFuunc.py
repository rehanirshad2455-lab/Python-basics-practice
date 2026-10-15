def checkPrime(a):
    if(a <= 1):
        return "not prime"
    for i in range(2, a):
        if(a % i == 0):
            return "not prime"
        
    return "is prime"

number = int(input("enter a number to check :"))
result = checkPrime(number)
print(result)


