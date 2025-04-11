class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show(self):
        return f'Owner: {self.owner}, Balance: {self.balance}'

    # Operator Overloading for + (Add Balances)
    def __add__(self, other):
        total = self.balance + other.balance
        return f'Total Balance after merging: {total}'

    # Operator Overloading for > (Compare Balance)
    def __gt__(self, other):
        return self.balance > other.balance
    
    # Operator Overloading for * (Multiplying Balance)
    def __mul__(self,other):
        total=self.balance*other.balance
        return f'Total Balance after multiplying: {total}'


a1 = Account("Majharul", 5000)
a2 = Account("Imran", 7000)

print(a1.show())
print(a2.show())

print(a1 + a2)      # Operator Overloading (+)

print(a1 > a2)      # Operator Overloading (>)
print(a2 > a1)

print(a1*a2)