students = {
    "Ali" : 99,
    "Ahmad" : 88,
    "Akbar" : 77,
    "Sara" : 78,
    "Rehan" : 77
}

print("All Students", students)

for name, marks in students.items():
    print(f"{name}, {marks}")

topper = max(students , key=students.get)

print("\n Topper" , topper)
print("Highest marks : " , students[topper])

total_marks = sum(students.values())
total_students = len(students)

average = total_marks / total_students
print("\n class average" ,average)

students["Ahmda"] = 90
print("\n Students Updated marks")
for name ,marks in students.items():
    print(f"{name} , {marks}")