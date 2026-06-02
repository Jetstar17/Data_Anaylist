#Random number does NOT mean a different number every time.
#Python Random module generates random numbers in Python.
#These are pseudo-random numbers means they are not truly random.
#  #This module can be used to perform random actions such as generating random numbers,
#  printing random a value for a list or string, etc. It is an in-built function in Python

#pythhon random randint() method
#return a number between 5 and 10 (bot+h included.)

import random


print(random.randint(1,10))  #return a number between 1 to 10


#return number between 3 (included) and 9 (not included)
print(random.randrange(3,9))

from numpy import random


y= random.randint(10)
print(y)


x = random.randint(999,10000)
print(x)

# when u give default value it will use between nos (0-1)
a = random.rand()  #0.28413296364946683
print(a)


# group of numbers using random function

b=random.randint(100, size=(5))
print(b)

# size (row, col)
c = random.randint(100, size=(3, 5))
print(c)



# random select no from list : use choice()
d = random.choice([3, 5, 7, 9])
print(d)

# selected no with list
# size (row, col)


x = random.choice([3, 5, 7, 4,11], size=(3, 5))
print(x)