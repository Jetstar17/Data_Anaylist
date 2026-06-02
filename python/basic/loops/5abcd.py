for i in range(0,5,1):
    for j in range(0,i + 1,1):
        print(chr(97 + j), end=" ")
    print()
    
    
"""
a 
a b 
a b c 
a b c d 
a b c d e
"""

for i in range(0, 10, 2):
    for j in range(i, -1, -2):
        # Converts 0->A, 2->C, 4->E, etc.
        print(chr(65 + j), end=" ")
    print()

'''
A 
C A 
E C A 
G E C A 
I G E C A
'''