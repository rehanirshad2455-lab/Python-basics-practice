inventory = {

"laptop" : 10,
"Mouse" : 5,
"KeyBoard" : 6,
"Monitor" : 3

}
print("=====================All products===============")
for product , quantity in inventory.items():
    print(f"{product} ,{quantity}")

new_product = input("\n Enter product name to add : ")
if new_product in inventory:
    print("ALready exist in inventory")
else:
    quantity = int((input))
inventory["Iron"] = 2
inventory["Mouse"] = 6
inventory.pop("laptop")
print(inventory.items())

search_items = input("Enter items to search")
if search_items in inventory:
    print("search item exist : " ,inventory[search_items])
else:
    print("does not exist")
