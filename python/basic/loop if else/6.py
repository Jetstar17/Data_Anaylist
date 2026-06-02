'''
1
10
10p
10p0
10p05
'''
for i in range(1,6,1):
    for j in range(1,i+1,1):
        if(j%2==0):
            print("0",end=" ")
        elif(j==3):
            print("p",end=" ")
        else:
            print(j,end=" ")
    print()
print()



