fruits=['grapes','apple','banana','gauava','papaya']

print(fruits[3])

popper= fruits.pop()

print(popper)
print(fruits)

fruits.remove('grapes')
print(fruits)

x=len(fruits)
print(f"x:{x}")

num=[10,20,[30,40],50]
print(f"num[2:3]:{num[2:3]}")
del num[2:3]
print(num)


fruits = ["apple", "banana", "apple", "orange", "banana"]
print(fruits)

fruits = ["apple", "banana", 10, 2.5, True]
print(fruits)

fruits = ["apple", 5, 3.14, False, ["mango", "grapes"], ("kiwi", "pear")]
print(fruits)

# len() returns total number of elements in the list
print(len(fruits))

# Accessing elements using positive index
print(fruits[0])   
print(fruits[1])   
print(fruits[4])  

# Accessing elements from the end using negative index
print(fruits[-1])  
print(fruits[-2])  

# Slicing returns a portion of the list
print(fruits[1:4])

# Step value is used to jump elements
print(fruits[0:6:2])

# Replacing multiple values using slicing
fruits[1:3] = [10, 20]
print(fruits)

# append() adds an element at the end of the list
fruits.append("orange")
print(fruits)

# remove() deletes the specified element from the list
fruits.remove(False)
print(fruits)

# reverse() reverses the order of elements
fruits.reverse()
print(fruits)

# Adding only numeric values from the list
total = 0
for item in fruits:
    if type(item) == int or type(item) == float:
        total += item

print(total)
 
# Multiplying only numeric values from the list
mul = 1
for item in fruits:
    if type(item) == int or type(item) == float:
        mul *= item

print(mul)
 

