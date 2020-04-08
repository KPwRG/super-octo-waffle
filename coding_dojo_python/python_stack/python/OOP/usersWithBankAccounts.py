class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.defaultInitialBalance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.int_rate = (self.int_rate / 365) * self.balance
            self.balance += self.int_rate
        return self

michael = User("Michael Myers", "themask@python.com")
walter = User("Walter White", "methman@python.com")
paul = User("Paul Lambert", "meatsauce@python.com")

michael.account.deposit(200).deposit(15).deposit(45).withdrawal(50).display_account_info()
walter.account.deposit(100).deposit(100).withdrawal(25).withdrawal(25).display_account_info()
paul.account.deposit(500).withdrawal(50).withdrawal(25).withdrawal(250).display_account_info()
