
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
email = input("Enter email: ")


subject1 = input("Enter subject 1 name: ")
marks1 = float(input("Enter marks for subject 1: "))


subject2 = input("Enter subject 2 name: ")
marks2 = float(input("Enter marks for subject 2: "))


subject3 = input("Enter subject 3 name: ")
marks3 = float(input("Enter marks for subject 3: "))


total = marks1 + marks2 + marks3
percentage = (total / 300) * 100   


print("\n------ STUDENT MARKS SHEET ------")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Email      :", email)

print(subject1, ":", marks1)
print(subject2, ":", marks2)
print(subject3, ":", marks3)

print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("--------------------------------")
