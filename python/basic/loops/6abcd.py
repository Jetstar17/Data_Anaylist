'''''
a
a b 
a b c 
a b c d 
a b c d e
'''
for i in range(0,5,1):
    for j in range(0,i + 1,1):
        print(chr(97 + j), end=" ")
    print() 
    
    
    
for i in range(0,5,1):
      for j in range(0,i + 1,1):
        print(chr(65 + j), end=" ")
      print()
"""
A
A B
A B C
A B C D
A B C D E
"""