numbers = [1,2,3,4,4,5,5,6,6,7,7,8,9,9,9,10,10]
new_numbers = []
for num in numbers:
    if num not in new_numbers:
        new_numbers.append(num)

print(new_numbers)