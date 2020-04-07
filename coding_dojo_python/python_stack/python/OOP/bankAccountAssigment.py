class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.defaultInitialBalance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}.")

    def yield_interest(self):
        if self.balance > 0:
            self.int_rate = (self.int_rate / 365) * self.balance
            self.balance += self.int_rate
        return self

account1 = BankAccount(0.01, 1000)
account2 = BankAccount(0.02, 2000)

account1.deposit(100).deposit(200).deposit(500).withdraw(1000).yield_interest().display_account_info()

account2.deposit(100).deposit(50).withdraw(1000).withdraw(500).withdraw(200).withdraw(100).yield_interest().display_account_info()
