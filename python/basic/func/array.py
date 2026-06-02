#An array is a special variable, which can hold more than one value at a time.
#ou can use the for in loop to loop through all the elements of an array.
#Python does not have built-in support for Arrays, but Python Lists can be used instead.
# work with arrays in Python you will have to import a library, like the NumPy library.
import array 
a = array.array('i', [2, 4, 5, 6])

print("First element is:", a[0])
print("Second element is:", a[1])
print("Third element is:", a[2])
print("Forth element is:", a[3])





print("last element is:", a[-1])
print("Second last element is:", a[-2])
print("Third last element is:", a[-3])
print("Forth last element is:", a[-4])
print(a[0],  a[1],  a[2],  a[3], a[-1], a[-2],  a[-3],  a[-4])
print(a)

# command for installing numpy module  py -m pip install numpy
import array as ar

numbers = ar.array('i', [1, 2, 3, 5, 7, 10])


#You can use the for in loop to loop through all the elements of an array.

cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)



# changing first element 1 by the value 0.
numbers[0] = 0
print(numbers)  # Output: array('i', [0, 2, 3, 5, 7, 10])

# changing last element 10 by the value 8.
numbers[5] = 8
print(numbers)  # Output: array('i', [0, 2, 3, 5, 7, 8])

# replace the value of 3rd to 5th element by 4, 6 and 8
numbers[2:4] = ar.array('i', [4, 6, 8])
print(numbers)  # Output: array('i', [0, 2, 4, 6, 8, 10])

# del function use in arra

number = ar.array('i', [1, 2, 3, 3, 4])
del number[2]  # removing third element
print(number)  # Output: array('i', [1, 2, 3, 4])

# Synatax for: len(array_name)
#The length of an array is always one more than the highest array index.
x = len(number)
print(f"length of array: {x}")

# concatnation of array
a = ar.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
b = ar.array('d', [3.7, 8.6])

c = a + b
print("Array c = ", c)

# sorting algorith (quick short)

import array as arr

arr= arr.array('i',[10,67,34,98,45])
for i in range(0,5):
     for j in range(i,5):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("sorted element...")
print(arr)