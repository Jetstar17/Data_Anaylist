set={'banana',390,'t',67.6}
print(set)


d = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(d)  

# Loop
for day in d:
    print(day)  # loop

# Add
d.add("Funday")  # add
print(d)

# Update
d.update(["Holiday", "Workday"])  # update
print(d)

# Discard
d.discard("Funday")  # discard
print(d)

# Remove
d.remove("Holiday")  # remove
print(d)

# Length
print(len(d))  # length


# If duplicate possible
d.add("Monday")  # duplicate
print(d)

# Clear
d.clear()  # clear
print(d)

# Pop
d = {"Monday", "Tuesday"}
popped = d.pop()  # pop
print(popped)
print(d)

# Sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {1, 3, 5, 7, 9}

# Intersection
print(A & B)  
print(A & B & C)  

# Union
print(A | B)  
print(A | B | C) 

# Intersection Update
A1 = A.copy()
A1.intersection_update(B)
print(A1) 

A2 = A.copy()
A2.intersection_update(B, C)
print(A2)  

# Difference
print(A - B)  
print(A - B - C)  

# Subtraction (same as difference)
print(A.difference(B))  
print(A.difference(B, C)) 



# Symmetric Difference 
print(A ^ B) 


print(A ^ B ^ C)  

#set comp
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday"}
Days3 = {"Monday", "Tuesday", "Friday"}

print(Days1 > Days2)
print(Days1 < Days2)
print(Days2 == Days3)

my_set = {1, 2, 3, 4, 5, 6, 12, 24}
n = int(input("Enter the number you want to remove "))
my_set.discard(n)
print("After Removing:", my_set)

set1 = {1, 2, 4, "John", "CS"}
set1.update(["Apple", "Mango", "Grapes"])
print(set1)

set1 = {"Peter", "Joseph", 65, 59, 96}
set2 = {"Peter", 1, 2, "Joseph"}
set3 = (set1|set2)
print(set3)


set1 = {23, 44, 56, 67, 90, 45}
set2 = {13, 23, 56, 76, "Sachin"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"Peter", "James", "Camroon", "Ricky", "Donald"}
set2 = {"Camroon", "Washington", "Peter"}
set3 = {"Peter"}

issubset = set1 >= set2
print(issubset)

issuperset = set1 <= set2
print(issuperset)

issubset = set3 <= set2
print(issubset)

issuperset = set2 >= set3
print(issuperset)

