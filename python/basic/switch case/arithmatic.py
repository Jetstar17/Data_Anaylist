a = int(input("enter first number:"))
b = int(input("enter second number:"))
ch = input("enter your choice..(+,-,,/,%,*,//)=")
match (ch):
    case '+':
        print("a+b=", {a + b})
        
    case '-':
        print(f" a-b: {a - b}")

    case '*':
        print(f" a*b: {a * b}")

    case '/':
        print(f" a/b: {a / b}")

    case '%':
        print(f" a%b: {a % b}")

    case '**':
        print(f" a*b: {a * b}")

    case '//':
        print(f" a//b: {a // b}")