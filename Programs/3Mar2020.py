# Old Style of programming
# class Test:
#     def func(self):
#         print("Hello World")


# obj = Test()
# obj.func()

# New Style of programming
# class Test1(object):

# ----------------------------------------------------
# class Person(object):
#     species = "Homo Sapiens"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getNameAge(self):
#         return self.name + " is " + self.age + " years old."

#     def getSpeciesNameAge(self):
#         return self.name + " is " + self.age + \
#             " years old and belongs to species " + self.species

#     def setHome(self, home):
#         self.__residence = home

#     def getResidence(self):
#         return self.__residence


# someHuman = Person("Adam", "100")
# anotherHuman = Person("Napoleon", "48")
# print(someHuman.getNameAge())
# print(someHuman.getSpeciesNameAge())
# print(anotherHuman.getSpeciesNameAge())
# anotherHuman.setHome("France")
# print(anotherHuman.getResidence())
# print(anotherHuman.__residence)
# print(anotherHuman.__dict__)  # All variable associated with the object
# print(anotherHuman._Person__residence)  # private variable

# ----------------------------------------------------

# Inheritance
class Animal(object):
    def __move(self):
        print("Le Animal Moves")


class Dog(Animal):
    def bark(self):
        print("Bhow! Bhow!")


class ThickCoatDog(Dog):
    def trim(self):
        print("Dog's hairs are getting trimmed.")

    def run(self):
        print("Run boy Run 2.")


class ViolentDog(Dog):
    def maul(self):
        print("Dog started scratching and biting.")

    def run(self):
        print("Run boy Run 1.")


class Mastiff(ThickCoatDog, ViolentDog):
    def wag(self):
        print("Dog wags its tail")


# bulldog = Dog()
# bulldog.bark()
# bulldog._Animal__move()  # This is created at the time of interpretation
# pitbull_dog = ViolentDog()
# pitbull_dog.maul()
# pitbull_dog.bark()

tibetan_mastiff = Mastiff()
tibetan_mastiff.run()
