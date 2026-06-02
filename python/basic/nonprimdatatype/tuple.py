tuple=(10,20,30)
print(tuple)

tup=(50,60)
print(tup+tuple)


my_tuple = ("Jay Khatwani", 21, 172.0, True, "Computer Engineering")

# Printing the tuple
print(my_tuple)

# Example 3: Empty Tuple
t1 = ()
print(t1)

# Example 4: Nested Tuple (tuple inside tuple or list)
t2 = ("apple", (1, 2, 3), ["mango", "banana"])
print(t2)

# Example 5: Creating a Tuple one item
t9 = ("Jay Khatwani")
print(t9)

# Example 6: Tuple using Constructor
t3 = ("python", 10, True)
print(t3)

# Example 7: Indexing of Tuple
print(t3[0])   # First element
print(t3[1])   # Second element

# Example 8: Length of Tuple
print(len(t3))

# Example 9: Negative Indexing
print(t3[-1])  # Last element
print(t3[-2])  # Second last element

# Example 10: Slicing the Tuple
print(t3[0:2])

# Example 11: Slicing with Jumping
print(t3[0:3:2])

# Example 12: Reverse the Tuple
rev_tuple = t3[::-1]
print(rev_tuple)

# Example 13: Duplicate values in Tuple
t5 = (1, 2, 3, 2, 4, 1)
print(t5)

# Example 14: Add data to Tuple (convert tuple to list and back)
temp_list = list(t3)
temp_list.append("Computer Engineering")
t3 = (temp_list)
print(t3)

# Example 15: Remove data from Tuple
temp_list = list(t3)
temp_list.remove(10)
t3 = (temp_list)
print(t3)

# Example 16: Delete a Tuple
t6 = (10, 20, 30)
del t6


# Example 17: Using loop in Tuple
for item in t5:
    print(item)

# Example 18: Join two Tuples
t7 = (1, 2, 3)
t8 = ("a", "b", "c")
t9 = t7 + t8
print(t9)

# Example 19: Multiply Tuple
t10 = (5, 6)
print(t10 * 3)

# Program: Take 5 inputs from user and store in a Tuple
user_list = []
for i in range(5):
    value = input("Enter value: ")
    user_list.append(value)

user_tuple = (user_list)
print(user_tuple)

