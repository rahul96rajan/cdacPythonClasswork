# Positional Arguments
# def my_sum(*args):
#     sum_all = 0
#     # print(args[0], args[2])  # Get individual values
#     for i in args:
#         sum_all += i
#     print(sum_all)


# my_sum(4, 5, 6, 7, 8, 6, 5, 2, 4, 5, 7, 5, 6)
#
# # Pass a list to arbitrary function using star (* expand the list to individual values)
# my_sum(*[5, 5, 5, 5])

# KV pair arbitrary func
# def print_kv(**args):
#     for key, value in args.items():
#         print(key, " :: ", value)
#
#
# #  f(**{str(k): v for k, v in kwargs.items()})
#
# my_dict = {"1": "apple", "2": "ball"}
# print_kv(**my_dict)
#
#
# # print_kv(a=1, b=2)
# # print_kv(1=a, 2=b)
#
#
# def fn(**kw):
#     print(kw, " ", len(kw))
#
#
# fn(a=2, b=3)

# Lambda Functions
# lm = lambda x, y: x ** y
#
# print(lm(2, 3))
#
# add = lambda a, r, g: a + r + g
#
# print(add(4, 5, 6))
#
#
# # Use of lambda function
# def funct(x):
#     return lambda y: x * y
#
#
# doubler = funct(2)
#
# print(doubler(2))
#
#
# def greet():
#     return "Hello"
#
#
# greet_lambda = lambda: "Hello"
#
#
# print(greet_lambda(), " ", greet())

# strip_and_upper = lambda s: s.strip().upper()
# print(strip_and_upper("  <rahul>  "))

# greeting = lambda x, *args, **kwargs: print(x, " -- ", args, " -- ", kwargs)
#
# print(greeting("H", "E", "L", "L", "O", wor="ld"))
from functools import reduce

# total = reduce(lambda a,x: a+x, [1,2,3,4,5,6])
#
# print(total)

# twos_multiple = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# print(twos_multiple)


# def fun1(a='abc', l1=['xyz']):
#     l1.append(a)
#     return l1
#
#
# lis1 = fun1("qwerty")
# lis2 = fun1("123")
# lis3 = fun1('q', [1, 2])
# print(lis1)
# print(lis1)
# print(lis3)
# lis4 = fun1("1235")
# print(lis4)


# maxim = reduce(lambda x, y: x if x > y else y, [5, 8, 19, 19.5, 4, 10, 11])
# print(maxim)


# Operators

import operator

# print(reduce(operator.add, [5, 8, 19, 19.5, 4, 10, 11]))
#
# print(reduce(operator.add, ["5", "8", "19", "19.5"]))  # add to concatenate
#
# # print palindromes
# print(list(filter(lambda x: x[::-1] == x, ["appple", "malayalam", "aaa", "q", ""])))
#
# print(list(filter(lambda x: x == "".join(reversed(x)), ["appple", "malayalam", "aaa", "q", ""])))


# Sorted
# print(sorted(["food", " Bar", "apple", ""], key=lambda s: s.strip().upper()))
# print(sorted(["food", " Bar", "apple", ""]))

# Map
print(sorted(map(lambda s: s.strip().upper(), ["food", " Bar", "apple", ""])))
