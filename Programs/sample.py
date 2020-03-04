'''
import math

print("Hello World")

a= complex(58,95)
print("Imaginary Part = " + str(a.imag) + "\nReal Part = " + str(a.real))
print(abs(a))

c= math.sqrt(a.imag**2 + a.real**2)
c=round(c,3)
'''
#print(c)
#5*8
#c = _
#print(c)

'''
import math

def cmp(a,b):
    return (a>b)-(a<b)

print(cmp(1,10))
'''
'''
a = "qbcdefgh@g""zGGg"[0:]

print(a.count("g",0,15))
print(len(a))

print("\tstring = %s  \n\tnumber = %d" %("qwerty",5.5))

sample ="e-mail is for the sole use of"
print(sample.title())

tuple = (45,85.6,'s',False,"qwetry")
print(tuple)

'''


#---Memory Management---

#Immutable
print("**Number(Integer) ID**")
a=90
b=a
print(id(a))
print(id(b))
a+=1
print(id(a))
print(id(b))


print("-"*50)
b=5
c=5
print(id(b))
print(id(c))
print(b == c)
print(b is c)

print("-"*50)

#Mutable
print("**Lists ID**")
li = [5,7,8,5,7]
print(id(li))
li+=[9,10]
print(id(li))

l1=[1,2,3]
l2=[1,2,3]
print(id(l2))
print(id(l1))
print(l1==l2)
print(l1 is l2)

l3=l1
print(l1 is l3)
l3.append(8)
print(l1)
print("-"*50)

#Exception with immutable objects - String Interning.
#Whats the exact range?
aq="pyhton is cool! pyhton is cool!"*5000
bq="pyhton is cool! pyhton is cool!"*5000
print("Id of aq = "+str(id(aq)))
print("Id of bq = "+str(id(bq)))
print(aq==bq)
print(aq is bq)
print("-"*50)

#Exception with immutable objects - Integer Caching, pyhton is caching intgers in the memory from -5 to 256 only
qa=257
qb=257
print("Id of qa = "+str(id(qa)))
print("Id of qa = "+str(id(qb)))
print(qa==qb)
print(qa is qb)
print("-"*50)

#Exception with immutable objects - Empty tuples
at=()
bt=()
print("Id of at = "+str(id(at)))
print("Id of bt = "+str(id(bt)))
att=(1,)
btt=(1,)
print("Id of at = "+str(id(att)))
print("Id of bt = "+str(id(btt)))
print(att is btt)
print("-"*50)

#Exception with immutable objects - Tricky case with operators
q1=[1,2,3]
print("Id of q1 = "+str(id(q1)))
q1+=[4]
print("Id of q1 = "+str(id(q1)))
q1=q1+[5]
print("Id of q1 = "+str(id(q1)))

print("-"*50)

#nested list
list = ["James",["B","o","n","d"]]
print(list[1][-1])
list[1][0] = 13
print(list)
del(list[1][0])
list.remove("James")
print(list)
print("-"*50)


list1 = ["B","o","n","d"]
print(list1)
list1.pop(1)
print(list)
print("-"*50)

#tuple packing- without brackets
tup=4,6,'end'
print(tup)
print("-"*50)

#tuple un-packing
r,s,v=tup
print(r,s,v)
print("-"*50)

#Dictionary
dict = {"a":"apple","b":"ball","b":"ball"}
print(dict)

