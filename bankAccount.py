class BankAccount:
    balance: float
    
    def __init__(self, balance: float):
        self.balance = balance
    
    def deposit(self, amount: float):
        self.balance += amount
        print("Dinero agregado a la cuenta")
        
    def withdraw(self, amount: float):
        self.balance -= amount
        print("Dinero retirado")
        
class SavingAccounts(BankAccount):
    min_balance: float
    
    def __init__(self, min_balance: float, balance: float):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if(self.balance - amount < self.min_balance):
            RuntimeError("La operación no se puede realizar porque la cuenta quedaría por debajo del balance mínimo permitido.")
        else:
            self.balance -= amount
        

