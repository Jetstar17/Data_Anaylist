#provide ready to use maths function
#min(),max(),power()
print(f" min: {min(80,20,40)}")
print(f" max: {max(50,70,110)}")
print(f" power : {pow(2,6)}")
print()


numbers=(100,300,200,49,55)
print(min(numbers))
print(max(numbers))
print()


# sqrt: square root
#Open the terminal window
#Check if PIP is installed
#Run the command pip install numpy
#Wait for the installation to complete
import math

print(math.sqrt(81))
print()

#
sqrt_no=math.sqrt(64)
print(f"square root : {sqrt_no}")
print("square root :" ,sqrt_no)
print()

# ceil: roundup the value and goes to nearest +
val=math.ceil(1.2)
print(f" ceil: {val}")
print()


# floor: roundup the value and  point value
print(f" floor: {math.floor(1.6)}") 
print()


#cos() function returns the cosine of value passed as argument.
print(f" cos(): {math.cos(30)}")
print()


# factorial : return x factorial as an integer.
# raises value error if x is not integral or is negative.
x=int (input("Enter the number for factorial."))
print(f" factorial of number: {math.factorial(x)}")
print()


#fsum (): return an accurate floating point sum of values in the iterable.
L=[10,20,30,40]
print(math.fsum(L))


