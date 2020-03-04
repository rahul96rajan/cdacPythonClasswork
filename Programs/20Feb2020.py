myDict = {"name":"Rahul Rajan", True:"False"}
print(myDict[True])
myDict[11]=[4,5,6] # adition
myDict["apple"]="saeb"
print(myDict)
print("-"*50)

#--popitem() remove the last element--
# print(myDict.popitem()) #return kv pair popped
# print(myDict)
# print(myDict.pop("name")) #return key popped
# print(myDict)
# print("-"*50)

# del myDict["name"]
# print(myDict)

#fromKeys()
# marks={}.fromkeys(["M","E","S"],1)
# print(marks)
# seq=(0,1,2)
# print(seq)
# ~ dictio = {}.fromKeys(seq,0)
# ~ print(dictio)
# print(marks.keys())
# ~ print(myDict.value())
# print("-"*50)

#Sets
# myS={1,"hi",(1,2,3)}
# print(myS)
#Set does not have duplicate values
# mySS= {1,1,1,1,1}
# print(mySS)
#Sets can not have mutable items
# mySSS={1,2,[3,4]} #Err
# print(mySSS)
# creating empty set is not allowed in python like set ={}, as it couldn't differetiatie with dict and set
# sss= set()
# print(type(sss))
# print("-"*50)

# *Set does not support indexing
# mySS.update([1,2,3,4])
# print(mySS)
# mySS.add(6)
# print(mySS)
#update could be done via list,set or tuples
# mySS.update([85,98],{78,96},(12,32))
# print(mySS)
# mySS.discard(85) # wont raise an error if value is not present
# mySS.remove(4) # will raise an error if value is not present
# print(mySS)
# mySS.pop()
# print(mySS)
# mySS.clear()
# print(mySS)
# mySS.update(['a','b','d','c','e'])
# print(mySS)
# mySS.pop()
# print(mySS)

#| or union()
#& or intersection()
#difference()
# ^ or symmetric_difference()
#isdisjoint()

#Frozen Sets - immutable sets
# F = frozenset([1,2,3,5])
# print(F)
# myDict = {}.fromkeys(F)
# print(myDict)


# sample program for number's sign

# num = int(input("Please input any integer : "))
# if num==0:
#     print("Zero")
# elif num<0:
#     print("Negative")
# elif num > 0:
#     print("Positive")
# else:
#     print("Please enter a valid integer!")


# Largest of three numbers

# num1 =  float(input("Please input the first number : "))
# num2 =  float(input("Please input the second number : "))
# num3 =  float(input("Please input the third number : "))
#
# if (num1>num2 and num1>num3):
#     print("Number 1 is the largest of the three.")
# elif (num2>num1 and num2>num3):
#     print("Number 2 is the largest of the three.")
# elif (num3>num1 and num3>num2):
#     print("Number 3 is the largest of the three.")
# elif (num1==num2==num3):
#     print("All three number are the same")


# *while-else
# range is used to generate a sequence of numbers (0 to n-1)
# print(range(10))
# print(range(-10,10))
# print(range(-50,50,10))

list = ["hello","word"]
for x in range(0,len(list)):
    print(x, list[x])




