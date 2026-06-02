def sum_ab():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a + b

s = sum_ab()
print("Sum:", s)

def circle_area():
    r = float(input("Enter radius: "))
    return 3.14 * r * r

area = circle_area()
print("Area of circle:", area)

def myself():
    name = input("Enter your name: ")
    return name

n = myself()
print("My name is", n)
