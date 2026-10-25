numbers = [12,66,44,99,101]
largest = max(numbers)
new_numbers = []
for num in numbers:
    if num!= largest:
        new_numbers.append(num)
if len(new_numbers) > 0:
    second_largest = max(new_numbers)
    print("Second largest = ", second_largest)
else:
    print("Does not exist")
