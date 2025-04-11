
class Bank:
    def __init__(self):
        self.ac_name='Majharul Islam'
        self._branch="Motijheel"
        self.__balance=5000
    
    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        self.__balance-=amount
    
    def print_info(self):
        return f'Account Name:{self.ac_name},Branch:{self._branch},Balance:{self.__balance}'
      

ac_1=Bank()

ac_1.deposit(2000)  # Depositing 2000
ac_1.withdraw(1000)  # Withdrawing 1000

# got error
# print(ac_1.__balance)
print(ac_1._Bank__balance)
print(ac_1.print_info())