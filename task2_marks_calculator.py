sub1 = int(input("Enter marks for subject1 : "))
sub2 = int(input("Enter marks for subject2 : "))
sub3 = int(input("Enter marks for subject3 : "))
sub4 = int(input("Enter marks for subject4 : "))
sub5 = int(input("Enter marks for subject5 : "))
sub6 = int(input("Enter marks for subject6 : "))
Total_marks = 600
obtained_marks = sub1+sub2+sub3+sub4+sub5+sub6
percentage = (obtained_marks / Total_marks) * 100 
print("Total Marks : ",Total_marks)
print("obtained Marks : ", obtained_marks)
print("percentage : ", percentage)