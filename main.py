class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} units. New balance: {self.balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

if __name__ == "__main__":
    account = BankAccount("123456789", 1000) 
    account.deposit(500)  
    account.withdraw(2000) 
    account.withdraw(700) 
