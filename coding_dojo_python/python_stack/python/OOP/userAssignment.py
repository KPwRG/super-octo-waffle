class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    

    def make_deposit(self, amount):
        self.account_balance += amount
        return self


    def make_withdrawal(self, amount):
        if amount > self.account_balance:
            print(f"Insufficient funds. Amount available for withdrawal is {self.account_balance}.")
        else:
            self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}.")

    # def transfer_money(self, other_user, amount):
    #     self.account_balance -= amount


# guido = User("Guido van Rossum", "guido@python.com")
# monty = User("Monty Python", "monty@python.com")
michael = User("Michael Myers", "themask@python.com")
walter = User("Walter White", "methman@python.com")
paul = User("Paul Lambert", "meatsauce@python.com")



# print(guido.name)	# output: Guido van Rossum
# print(monty.name)	# output: Monty Python


# guido.make_deposit(100)
# guido.make_deposit(200)
# monty.make_deposit(50)
# print(guido.account_balance)	# output: 300
# print(monty.account_balance)	# output: 50

# guido.make_withdrawal(75)
# monty.make_withdrawal(25)

# guido.display_user_balance()
# monty.display_user_balance()

# michael.make_deposit(200)
# michael.make_deposit(15)
# michael.make_deposit(45)
# michael.make_withdrawal(50)
# michael.display_user_balance()

# walter.make_deposit(100)
# walter.make_deposit(100)
# walter.make_withdrawal(25)
# walter.make_withdrawal(25)
# walter.display_user_balance()

# paul.make_deposit(500)
# paul.make_withdrawal(50)
# paul.make_withdrawal(25)
# paul.make_withdrawal(250)
# paul.display_user_balance()

michael.make_deposit(200).make_deposit(15).make_deposit(45).make_withdrawal(50).display_user_balance()
walter.make_deposit(100).make_deposit(100).make_withdrawal(25).make_withdrawal(25).display_user_balance()
paul.make_deposit(500).make_withdrawal(50).make_withdrawal(25).make_withdrawal(250).display_user_balance()
