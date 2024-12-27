# class person:
#     def __init__(self, age, username, salary):
#         self.username = username
#         self.salary = salary
#         self.age = age
#
#     def getusername(self):
#         return self.username
#
#     def getage(self):
#         return self.age
#
#     def getsalary(self):
#         return self.salary
#
# username = input("Enter your username =")
# age = input("enter your age =")
# salary= input("Enter your salary =")
#
# p = person(age,username,salary)
# print(f"your username is '{p.getusername()}'")
# print(f"your '{p.getage()}' years old")
# print(f"your salary is '{p.getsalary()}' per month")

# class Automobile:
#     def __init__(self, colour, make, speed, ):
#         self.colour = colour
#         self.make = make
#         self.speed = speed
#
#     def getcolour(self):
#         return self.colour
#
#     def getmake(self):
#         return self.make
#
#     def getspeed(self):
#         return self.speed
#
#     def getgear(self):
#         if self.speed <= 20:
#             return 1
#
#         if 20 < self.speed <= 40:
#             return 2
#
#         if 40 < self.speed <= 80:
#             return 3
#         if 80 < self.speed <= 100:
#             return 4
#         else:
#             print("gear can't detect")
#
#
# colour = input("Enter colour of the car =")
# company = input("Enter the name of company =")
# speed = int(input("Enter speed of the car ="))
# a = Automobile(colour, company, speed)
# print(f"The car is '{a.getmake()}' group of company")
# print(f"The car is '{a.getcolour()}' colour")
# print(f"the speed of the car is {a.getspeed()}KM per hr")
# print(f"The car is in '{a.getgear()}'th gear")


