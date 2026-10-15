fruits = ["mango", "banana", "orange" , "grapes", "strawebery"]
for fruit in fruits:
    print(fruit)
search_fruit = input("Enter fruit to search: ").lower()
if(search_fruit in fruits):
    print(search_fruit ,"found")
else:
    print("This fruit",search_fruit,"was not found")