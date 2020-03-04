# Generators


# def gen_func():
#     for i in range(10):
#         yield i
#
#
# for it in gen_func():
#     print(it)

##
# def simple_func():
#     yield 1
#     yield 2
#     yield 3


# for it in simple_func():
#     print(it)


# x = simple_func()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(simple_func().__next__())
# print(simple_func().__next__())


# # Infinite Sequence - won't consume memory
#
# def infinite_seq():
#     num =0
#     while True:
#         yield num
#         num += 1
#
# gen = infinite_seq()
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())
# while True:
#     print(gen.__next__())


# # Fibonacci Series
# def fib(end):
#     a = b = 1
#     for i in range(end):
#         yield a
#         a, b = b, a + b
#
#
# for x in fib(10000):
#     print(x)

# ------------------------------------------------------------------------------------------------

# # Generator Comprehensions ///r to list comp, diff is ()
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# gen1 = (x for x in list1 if (x % 2 == 0))
# print(gen1)
# for x in gen1:
#     print(x)

# ------------------------------------------------------------------------------------------------

# gen1 = (x for x in range(0,11))
# gen2 = (x for x in range(0,11))
# print(5 in gen1)
# print(5 in gen1)  # The function call is yielded at 5 in the last statement
# print(sum(gen1), sum(gen2))

# # Table of a number using generator
# def math_table_generator(num, end):
#     for i in range(1, end+1):
#         # yield str(num) + " X " + str(i) + " = " + str(num*i)
#         yield ("{0}" + " X " + "{1}" + " = " + "{2}").format(num, i, num*i)
#
#
# def main():
#     num = int(input("Please input the value: " ))
#     limit = int(input("Please input the limit: " ))
#
#     for x in math_table_generator(num, limit):
#         print(x)
#
#
# main()

# ------------------------------------------------------------------------------------------------

# Regular Expressions
# import re

# from re import findall, compile

# char_between_a_and_e = compile("[a-eA-E]")
string = "Hello I am Newton's Apple sprouted in Lincolnshire, 1687/21/01 05:10:36. I helped in discovery_of_Gravity"
# print(char_between_a_and_e.findall(string))
#
# # \d = [0-9]
# numbers_re = compile("[0-9]+")
# print(numbers_re.findall(string))
#
# # \w = [a-zA-Z0-9_]
# alpha_numeric_underscores = compile("\w+")
# print(alpha_numeric_underscores.findall(string))
# # capital are inverse of the small letters
# compliment_alpha_numeric_underscores = compile("\W+")
# print(compliment_alpha_numeric_underscores.findall(string))

# string_ab = "a abbabbbabbbbbababab"
# ab = compile("ab+")
# print(ab.findall(string_ab))

# RE split
# from re import split,IGNORECASE
#
# print(split("[A]", string, flags=IGNORECASE))


# # RE Sub
# from re import sub, subn
#
# print(sub("\s*\d+", "<digits>", string, 3))
# print(len(subn("\s*\d+", "<digits>", string)))

# Find words in list which ends with 'ed'
import re

# list1 = ["ededed", "started", "fly", "cool", "hot-headed", "bored"]
# list2 = [w for w in list1 if re.search("ed", w)]
# print(list2)


# Find
# lis1 = ["abjectly", "adjuster", "dejected", "abandoned"]
# print([w for w in lis1 if (re.search("^..j..t..$", w))])

# list_e_mail= ["email", "e-mail", "e_mail"]
# print([w for w in list_e_mail if (re.search("^e-?_?mail$", w))])
# print(sum([1 for w in list_e_mail if (re.search("^e-?_?mail$", w))]))

# lis1 = ["abjectly", "adjuster", "dejected", "abandoned"]
# print([w for w in lis1 if (re.search("^[abc][be]", w))])

# ^m+i+n+e+$

# (^\d+\.\d+$)|(^\.\d+$)
decimals = ["45.85", "5", "5.25", "0.96", ".", ".6", "0.6"]
print([w for w in decimals if (re.search("(^\d+\.\d+$)|(^\.\d+$)", w))])