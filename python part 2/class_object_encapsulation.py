# class Person:
#     name = None
#     age = None
#     salary = None
#
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def setAge(self, age):
#         self.age = age
#
#     def getAge(self):
#         return self.age
#
#     def getSalary(self, salary):
#         self.salary = salary
#
#     def getSalary(self):
#         return self.salary
#
#
# p = Person()
# p.setName("raghav")
# p.setAge(22)
# p.setSalary(80000)
#
# print(p.getName(), p.getAge(), p.getSalary())
import asyncio


# practice of clas and objects
# class raghavsmarks:
#     english = None
#     hindi = None
#     bst = None
#     eco = None
#     account = None
#
#     def setenglish(self, english):
#         self.english = english
#
#     def getenglish(self):
#         return self.english
#
#     def sethindi(self, hindi):
#         self.hindi = hindi
#
#     def gethindi(self):
#         return self.hindi
#
#     def setbst(self, bst):
#         self.bst = bst
#
#     def getbst(self):
#         return self.bst
#
#     def seteco(self, eco):
#         self.eco = eco
#
#     def geteco(self):
#         return self.eco
#
#     def setaccount(self, account):
#         self.account = account
#
#     def getaccount(self):
#         return self.account
#
#
# p = raghavsmarks()
# p.setenglish(50)
# p.sethindi(78)
# p.setbst(72)
# p.seteco(50)
# p.setaccount(49)
# print("your account,s marks is =", p.getaccount())
# print("your economics marks is =", p.geteco())
# print("your business studies marks is =", p.getbst())
# print("your hindi marks is =", p.gethindi())
# print("your english marks is =", p.getenglish())
# print("note:- your account is very weak.. i hope you give more efforts in study.....!")


# account in class and object

class account:
    account_type = None
    balance = None
    number = None

    def setaccount_type(self, account_type):
        self.account_type = account_type

    def getaccount_type(self):
        return self.account_type

    def setbalance(self, balance):
        self.balance = balance

    def getbalance(self):
        return self.balance

    def setnumber(self, number):
        self.number = number

    def getnumber(self):
        return self.number


p = account()
p.setaccount_type("Current")
p.setbalance(500)
p.setnumber(490456358078)
print("your account number is =",p.getnumber())
print("you have = $",p.getbalance())
print(f"your account is '{p.getaccount_type()}' Account")
