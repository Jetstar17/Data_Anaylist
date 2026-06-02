import lamdaa

def demo():
    a=10
    b=20
    print(a+b)
    
demo()

sum=lambda a,b: a+b
demo=lambda a,b: a+b
print(sum(10,20))