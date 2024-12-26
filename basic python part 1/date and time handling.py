# date and time handling
import datetime
from datetime import date

# x = datetime.datetime.now() # for today day and date and year
# print(x.year)
# print(x.strftime("%D")) #A=day : B=month : c=? : D=date/mont/year

# x = datetime.datetime(2006,1,25) # for date you want to write


# project of calculate your age using date and time

years = date.today().year
birth= int(input("enter your birth years = "))
age = years -birth
print(f"your {age} years old")