# raw string vs normal string
# normal_str = "This is a \nnormal string"
# print(normal_str)
# raw_str = r"This is a \nraw string"
# print(raw_str)
# re.escape()
# re.search()

import re

# regex = r"([a-zA-Z]{3}) (\d+)"
# string = "Feb 28 aFeq 27 a"
# exp1 = re.search(regex, string)
# print(exp1)
# if exp1!=None:
#     print("Match index : ", exp1.start(), exp1.end())
#     print("Match Group : ", exp1.group())
#     print("Match Group 1 : ", exp1.group(1))
#     print("Match Group 2 : ", exp1.group(2))

# re.match vs re.search

# exp1 = re.match(regex, string)
# print(exp1)
# if exp1!=None:
#     print("Match Group : ", exp1.group())
#     print("Match Group 1 : ", exp1.group(1))
#     print("Match Group 2 : ", exp1.group(2))

# \b : word boundaries \B
# reg_b = re.compile(r"\bclass\b")
# reg_B = re.compile(r"\Bclass\B")
str2= "classification of subclasses in a class 175 class class y y end"
# print(reg_b.findall(str2))
# print(reg_B.findall(str2))

# ^ inside [] means comppliment but in front
# reg_7 = re.compile(r"[^7]")
# print(reg_7.findall(str2))

# repeat a  word r"\b(\w+)\s+\1\b" using groups
# reg_double = re.compile(r"\b(\w+)\s+\1\b")
# print(reg_double.findall(str2))
# print(reg_double.search(str2).group())

# Group naming
# '?P<name>
reg_double1 = re.compile(r"\b(?P<word>\w+)\s+(?P=word)\b")
# reg_double1 = re.compile(r"\b(?P<word>\w+)\s+(?P=word)\b")
print(reg_double1.findall(str2))
print(reg_double1.search(str2).group())