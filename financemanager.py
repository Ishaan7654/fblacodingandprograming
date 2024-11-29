class FinanceManager():
    def __init__(self, name):
        self.user = name
        self.balance = 0
    
    def add_to_balance(self, amount):
        self.balance += amount
    
    def remove_from_balance(self, amount):
        self.balance -= amount
