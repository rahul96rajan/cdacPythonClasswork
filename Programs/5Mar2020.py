# # Raise an Error/Exception
# try:
#     age = int(input("Please enter some age : "))
#     if (age < 18):
#         raise ValueError
#     if (age < 0 or age > 120):
#         raise TypeError
#     else:
#         print("Valid age.")
# except (ValueError, TypeError):
#     print("Not a valid age.")

#  -----------------------------------------------

# # User defined Error/Exception
# class Error(Exception):  # our base class for errors
#     pass


# class ValueTooSmallError(Error):
#     pass


# class ValueTooLargeError(Error):
#     pass


# number = 10

# while(True):
#     try:
#         inum = int(input("Enter a number : "))
#         if inum < number:
#             raise ValueTooSmallError
#         elif inum > number:
#             raise ValueTooLargeError
#         print("Correct Guess!")
#         break
#     except ValueTooLargeError:
#         print("--> Value Too Large")
#     except ValueTooSmallError:
#         print("--> Value Too Small")


# class InapropriateAgeCustomError(Exception):
#     def __str__(self):
#         return "InapropriateAgeCustomError"


# try:
#     age = int(input("Please enter some age : "))
#     if (age < 18):
#         raise InapropriateAgeCustomError
#     if (age < 0 or age > 120):
#         raise InapropriateAgeCustomError
#     else:
#         print("Valid age.")
# except InapropriateAgeCustomError as e:
#     print("Not a valid age.", "\nError caught : ", e)


# -----------------------------------------------------------------------

# Deleting and Adding attributes in Objects

# class ComplexNumber(object):
#     def __init__(self, r=0, i=0):
#         self.r = r
#         self.i = i

#     def getData(self):
#         print("number : {0}+{1}j".format(self.r, self.i))


# c1 = ComplexNumber(5, 8)
# c2 = ComplexNumber(6, 9)
# c1.getData()
# c1.a = 99
# print(c1.a)
# del c2.i
# print(c1.i)

# ----------------------------------------------------------------------

# class Vehicle(object):
#     kind = "Car"
#     bath_number = 5

#     def __init__(self, manufacturer, model):
#         self.manufacturer = manufacturer
#         self.model = model

#     def __str__(self):
#         return "{0} {1}".format(self.manufacturer, self.model)


# print(carOne.__dict__)
# carOne = Vehicle('Toyota', 'Corolla')
# print(carOne, "Type : ", carOne.kind)
# carTwo = Vehicle("Honda", "Civic")
# print(carTwo, "Type : ", carOne.kind)
# Vehicle.kind = "Scrapped"

# print("Car One Type:", carOne.kind, ", Car Two Type:", carTwo.kind)
# carOne.kind = "QWERTYY"
# print(carOne.kind)
# print(carTwo.kind)
# Vehicle.kind = "Scrapped2"
# print(carOne.kind)
# print(carTwo.kind)
# # print(carOne.bath_number)


# for mutable
# class Test(object):
#     lst = [1, ]


# t1 = Test()
# t2 = Test()
# print(t1.lst, t2.lst)
# t1.lst.append(2)
# print(t1.lst, "\n", t2.lst)

# Output Question
# class Fruit(object):
#     def __init__(self, price):
#         self.price = price


# obj = Fruit(50)
# obj.quant = 10
# obj.bag = 2
# print(obj.quant + len(obj.__dict__))


# ------------------------------------------------------------------

# with open("C:/Users/rahulrajan/Documents/scripts/cdacPythonClasswork/"
#           + "Programs/files/sample1.txt", "a", encoding='UTF-8') as fp:
#     fp.write("Line 1\n")
#     fp.write("Line 2\n")
#     fp.write("Line 3\n")

with open("C:/Users/rahulrajan/Documents/scripts/cdacPythonClasswork/Programs/"
          + "files/sample1.txt", "r", encoding='UTF-8') as fp:
    print(fp.read(2))
    print(fp.read(2))
    print(fp.read(2))
    print(fp.read())
    print("When Cursor at the end.", fp.read())
    fp.seek(0)  # To reposition the cursor
    print(fp.read())
