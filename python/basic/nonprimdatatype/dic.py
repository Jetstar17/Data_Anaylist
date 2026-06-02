dic={'color':'black',
     'speed':'slow',
     'food':{
             'fruit':'mango',
             'veg':'batata'
            }
    } 
print(dic['color'])
print(dic['food']['veg'])

a={"id":1,"name":"jay","email":"jay@12","age":"20",
   "a":[1,2,3]
  }
print(a)

#length of dic
print(len(a))

print(a)

#all keys
print(a.keys())

#values
print(a.values())

#get any specific
print(a.get("name"))

#change val
a["age"]= 30
print(a)

#pop element
a.pop("name")
print(a)

#add new
a.update({"gender":"male"})
print(a)

#delete
'''''
del a
print(a)
'''
 


#clear
''''
a.clear
print(a)
'''
#concanditenation
dic={"x":"7"}
dic2={"y":"8"}

for d in (dic,dic2): a.update(d)
print(a)
 
 