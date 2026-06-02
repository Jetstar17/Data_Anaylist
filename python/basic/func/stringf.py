#-4-3-2-1
string='handcomputer education'
    #   012345678910


stringstr1= string[5:10]   #5 index to 9 

print(stringstr1)

print(string[:10])   #start with 0 index end with 9
print(string[5:])   #start with 5 end with last index
print(string[:])    #full string start with 0 end with last index
print(string[-8:-3])  #start with -8 and end with -4
print(string[5::2])  #start with 5 and jump 2 step
print('string[::2]= ',string[::2]) #full string will be print with 2 stepouted.
print('string[:-1]= ',string[:-1])#start with 0 index end with last index -1.
print('string[::-1]= ',string[::-1])#reverse string with one stepedout.
print('string[::-2]= ',string[::-2])#reverse string with two stepedout.


# '''
# #string slice
# string='H&B COMPUTER EDUCATION from Gandhinagar.'

print('string[:2]= ',string[:2])#string will be print only 0 index to 2 index alphabets.

print('string[0:20]= ',string[0:20]) 
print('string[20:]= ',string[20:])