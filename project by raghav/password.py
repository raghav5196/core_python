import random
char = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqustuvwxyz@#$%&"
Length = int(input("Enter Length of the password ="))
password=""

for i in range(Length):
    password+=random.choice(char)
print(password)

balance = int(input("Enter a balance amount="))
num = int(input("Enter a deposit amount = "))

balance+=num
print(f"The amount after deposit {balance}")

balance-=num
print(f"The amount after withdrawal{balance}")