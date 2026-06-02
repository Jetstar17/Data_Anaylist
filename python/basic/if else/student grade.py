m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))

total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100

if percentage >= 75:
    print("Rank: Distinction")
elif percentage >= 60:
    print("Rank: First Class")
elif percentage >= 50:
    print("Rank: Second Class")
elif percentage >= 35:
    print("Rank: Pass Class")
else:
    print("Rank: Fail")
