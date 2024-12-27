# class Account:
#     def __init__(self, balance):
#         self.balance = balance
#         withdrawal = None
#         deposit = None
#
#     def setwithdrawal(self, withdrawal):
#         self.withdrawal = withdrawal
#         self.balance -= withdrawal
#
#     def getwithdrawal(self):
#         return self.withdrawal
#
#     def setdeposit(self, deposit):
#         self.deposit = deposit
#         self.balance += deposit
#
#     def getdeposit(self):
#         return self.deposit
#
#     def getbalance(self, balance):
#         return self.balance
#
#
# a = Account(1000)
#
# a.setdeposit(100)
# print(f"your account amount after debit ", a.getbalance(00))
#
# a.setwithdrawal(500)
# print("your account amount after credit ", a.getbalance(00))


class Account:
    def __init__(self, balance, withdrawal, deposit):
        self.balance = balance
        self.withdrawal = withdrawal
        self.deposit = deposit

    def getwithdrawal(self):
        return self.withdrawal
        # self.balance -= withdrawal

    def getdeposit(self):
        return self.deposit
        # self.balance += deposit

    def getbalance(self, balance):
        # return self.balance
        if self.balance - self.withdrawal:
            print(self.balance)

        if self.balance - self.withdrawal:
            print(self.balance)

balance = int(input("Enter a Balance  ="))
withdrawal = int(input("Enter amount of withdraw ="))
deposit = int(input("Enter amount of deposit  ="))

a = Account(balance,deposit, withdrawal)

# print(a.getbalance(1000))
# print("ram",a.getwithdrawal())
# print(a.getdeposit())
print("your account amount after credit ", a.getbalance(0))
