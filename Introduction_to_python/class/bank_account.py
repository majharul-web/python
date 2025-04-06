class BankAccount:
    # Class Attribute
    bank_name = "ABC Bank"

    # Constructor (Instance Attributes)
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit Method
    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}. New Balance = {self.balance}')

    # Withdraw Method
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Balance')
        else:
            self.balance -= amount
            print(f'Withdrawn {amount}. New Balance = {self.balance}')

    # Representor Method
    def __repr__(self):
        return f'Account Holder: {self.account_holder}, Balance: {self.balance}, Bank: {BankAccount.bank_name}'


# Create Object
my_account = BankAccount("Majharul", 5000)

print(my_account)         # Before Transaction
my_account.deposit(2000)  # Deposit Money
my_account.withdraw(1000) # Withdraw Money
my_account.withdraw(7000) # Try to Withdraw More than Balance
print(my_account)         # After Transaction
