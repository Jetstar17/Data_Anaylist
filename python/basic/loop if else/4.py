'''''
0
02
020
0204
02040
'''
for i in range(1,6,1):
    for j in range(1,i+1,1):
        if(j%2!=0):
            print(0,end=" ")
        else:
            print(j,end=" ")
    print()