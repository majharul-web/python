class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def bank_info(self):
        return f'Bank: {self.name}, Location: {self.location}'
    
    def loan_interest(self):
       raise NotImplementedError
        # return "General Loan Interest: 5%"


class IslamicBank(Bank):
    # method overriding
    def loan_interest(self):
        return "Islamic Bank Loan Interest: 3% (Profit Share)"

    def service_info(self):
        return "Special Service: Islamic Banking Facility"


b1 = IslamicBank("Islami Bank", "Dhaka")
print(b1.bank_info())
print(b1.loan_interest())
print(b1.service_info())
