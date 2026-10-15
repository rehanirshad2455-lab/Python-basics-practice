def  fibonacci(n):
    series = []
    a = 0
    b = 1
    for i in range(n):
        series.append(a)
        a,b = b, a+b
    return series

terms = int(input("entre a number of terms"))
result = fibonacci(terms)
print(result)