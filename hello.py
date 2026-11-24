
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transition = []

    def deposit(self, amount):
        self.balance += amount
        self.transition.append("Deposited: " + str(amount))
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transition.append("Withdrawn: " + str(amount))
            print("Withdraw amount:", amount)
        else:
            print("Insufficient balance")

    def checkbalance(self):
        print("Current Balance:", self.balance)


account1 = BankAccount("Ali", 5000)

while True:
    print("================================================")
    print("=============== BANK MENU ======================")
    print("1: Deposit")
    print("2: Withdraw")
    print("3: Check Balance")
    print("4: Exit")

    choose = int(input("Enter the Number: "))

    if choose == 1:
        amount = int(input("Enter amount: "))
        account1.deposit(amount)

    elif choose == 2:
        amount = int(input("Enter amount: "))
        account1.withdraw(amount)

    elif choose == 3:
        account1.checkbalance()

    elif choose == 4:
        print("Thank you for visiting!")
        break

    else:
        print("Invalid number")
