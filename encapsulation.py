class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_balance(self):
        return self.__balance
    
    def set_account_holder_name(self, name):
        self.__account_holder_name = name

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

account = BankAccount("123456", "Fahimul Haque", 147570)
print(account.get_balance())  # Output: 1000
account.deposit(30)          # Output: Deposited: 500. New balance: 1500
account.withdraw(4700000)        # Output: Insufficient funds or invalid amount.
account.withdraw(47000)         # Output: Withdrew: 300. New balance: 1200
