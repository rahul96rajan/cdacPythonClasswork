# import os
# import shutil

# print(os.getcwd())
# print(os.getcwdb())
# os.chdir("C:\\Users\\rahulrajan\\Music")
# print(os.getcwd())
# print(os.listdir())
# os.mkdir("sample")
# os.rename('sample', 'new_sample')
# open("C:\\Users\\rahulrajan\\Music\\new_sample\\"
#      + "sample.txt", "w", encoding='UTF-8')
# os.remove(os.getcwd() + "\\new_sample\\sample.txt")
# shutil.rmtree("C:\\Users\\rahulrajan\\Music\\new_sample")


#  ------------------------------------------------------------------------

# print(os.path.join("C:\\", "Users", "rahulrajan", "Music"))
# print(os.path.split("C:/Users/rahulrajan/Music/r1"))
# print("Path Exists =>", os.path.exists("C:/Users/rahulrajan/Music"))
# print("Is this directory =>", os.path.exists("C:/Users/rahulrajan/Music"))
# for roots, dirs, files in os.walk("C:/Users/rahulrajan/Music"):
#     print(" Root: ", roots, " Length Directory: ", len(dirs),
#           " Length Files: ", len(files))

# import mysql.connector

# myconn = mysql.connector.connect(host="localhost", user="root",
#                                  password="root", database="emp")
# cur = myconn.cursor()
# sql = "insert into the employee(ename,id,sal) values(%s,%s,%s)"
# val = ("John", 110, 505050)
# try:
#     cur.execute(sql, val)
#     myconn.commit()
# except Exception:
#     myconn.rollback()

# print(cur.rowcount())

import add_sub as a
import mult_div as d

# print(a.add_r(5, 6))
# print(a.sub_r(8, 6))
print(d.mult_r(5, 6))