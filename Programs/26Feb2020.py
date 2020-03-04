# scope resolution


# def location():
#     global place  # This would enable the function to point to global space for this specific object
#     loc = "Sector 62"
#     place = "New Delhi"
#
#
# place = "Noida"
# print(place)
# location()
# print(place)


# -------------------------------------------------------------------------------

# globals() and locals()
# x = 50
#
#
# def fun():
#     x = 20
#     print(x)  # 20
#     print('x' in globals())  # quotes are mandatory
#     print('x' in locals())
#     print(globals()['x'])  # 50
#     globals()['x'] = 60
#     print(globals()['x'])
#
#
# print(x)  # 50
# fun()
# print(x)


# -------------------------------------------------------------------------------


# def f():
#     city = "New Delhi"
#
#     def g():
#         nonlocal city  # global, nonlocal not available to non nested functions
#         city = "Noida"
#
#     print("Before Calling G() : ", city)
#     g()
#     print("After Calling G() : ", city)
#
#
# f()
# print("City val from globals: ", city)

# -------------------------------------------------------------------------------

# def f():
#     city = "New Delhi"
#
#     def g():
#         # nonlocal city  # global, nonlocal not available to non nested functions
#         city = "Noida"
#
#         def h():
#             nonlocal city
#             city = "Chandigarh"
#
#         print("inside G() before calling h() : ", city)
#         h()
#         print("inside G() after calling h() : ", city)
#
#     print("Before Calling G() : ", city)
#     g()
#     print("After Calling G() : ", city)
#
#
# f()
# print("Global City: ", city)


# -------------------------------------------------------------------------------


# Comprehension

# List Comprehension
# input_list = [1, 2, 3, 4, 5, 6, 7]
# odd_list = [x for x in input_list if(x%2==1)]
# print(odd_list)
#
# l1 = [x**2 for x in range(1, 11)]
# print(l1)

# Dict Comprehension
# input_list = [1, 2, 3, 4, 5, 6, 7]
# dict_cube = {x: x ** 3 for x in input_list if x % 2 == 1}
# print(dict_cube)

# state = ["Rajasthan", "Punjab", "Gujrat"]
# capital = ["Jaipur", "Chandigarh", "Gandhi Nagar"]
# dict_s_c = {x: y for (x, y) in zip(state, capital)}
# print(dict_s_c)

# Set Comprehensions
# input_set = {1, 2, 3, 4, 5, 6, 7, 8}
# input_list = [1, 2, 3, 4, 5, 6, 7]
# set1 = {x**2 for x in input_set}
# print(set1)


# -------------------------------------------------------------------------------


# Hack - passing multiple list in map
# a = range(10, 20)
# b = range(0, 10)
# c = range(30, 40)
# l = set(map(lambda x, y, z: x * y * z, a, b, c))
# print(l)
#
# # Hack - if else in lambda
# f = lambda x: x > 100 and 'big' or 'small'
# for i in (1, 10, 99, 100, 101, 110):
#     print (i, 'is', f(i))
