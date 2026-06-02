a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a <= b and a <= c and a <= d:
    print("Smallest number is:", a)
elif b <= a and b <= c and b <= d:
    print("Smallest number is:", b)
elif c <= a and c <= b and c <= d:
    print("Smallest number is:", c)
else:
    print("Smallest number is:", d)
