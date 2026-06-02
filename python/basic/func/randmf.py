# recursion function means function call bt itself / function call in itself
# replace loop
# memory occupation is more than loop and time consuming
# better is use loop

# factorial of given number
def factorial(n):
    
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# Driver Code
num = 5
print("Factorial of",num,"is",factorial(num))