# basic of exception handling
from logging import exception

# a = 10
# b = 0
# try:
#     c = a / b
#     print(c)
# except:
#     print("number can't be divided")
# print("raghav")

##try except using else

# a = 10
# b = 1
# try:
#     c = a / b
#     print(c)
# except:
#     print("number can't be divided")
# else : #uper exception nhi ho ga toh hi 'else' kaam kre ga
#     print("uper exception nhi ho ga toh hi 'else' kaam kre ga ")

# try exception using finally
# a = 10
# b = 0
# try:
#     c = a / b
#     print(c)
# except: #isme uper kuch bhi ho exception ho ya na ho kuch fark nhi pad ta hai
#     print("number can't be divided")
# finally:
#     print("isme uper kuch bhi ho exception ho ya na ho kuch fark nhi pad ta hai")

# raise Exception
# try:
#     number = int(input("Enter Your number here :"))
#
#     if number < 10:
#         raise Exception(number)
#     print("number id invalid")
#
# except Exception as e:
#     print(e)
# print("raghav")

# try:
#     a=int(input("enter a  number = "))
#     b = int(input("enter a divided number ="))
#     c=a/b
# except ValueError:
#     print("Value is not int type ")
# except ZeroDivisionError:
#     print("number can't divide by zero")
# else :
#     print(c)
