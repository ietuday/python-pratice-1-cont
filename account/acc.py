class Account:

    def __init__(self, filePath):
        self.filePath = filePath
        with open(filePath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filePath, 'w') as file:
            file.write(str(self.balance))


account = Account('account/balance.txt')
print(account.balance)
account.withdraw(100)
account.commit()
