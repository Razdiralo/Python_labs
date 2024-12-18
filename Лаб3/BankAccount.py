class BankAccount:
    accounts_quantity = 0

    MIN_BALANCE = 100

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        BankAccount.accounts_quantity += 1

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"Счет {self.account_number} пополнен на {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= BankAccount.MIN_BALANCE:
                self.balance -= amount
                print(f"Снято {amount} со счета {self.account_number}. Текущий баланс: {self.balance}")
            else:
                print(f"Операция отклонена. Баланс после снятия не должен быть меньше {BankAccount.MIN_BALANCE}.")
        else:
            print("Сумма снятия должна быть положительной.")

    def check_balance(self):
        return f"Текущий баланс счета {self.account_number}: {self.balance}"



account = BankAccount("12345", 500)
print(account.check_balance())

account.deposit(200)
print(account.check_balance())

account.withdraw(650)
print(account.check_balance())

account.withdraw(500)
print(account.check_balance())

print(f"Количество созданных счетов: {BankAccount.accounts_quantity}")
