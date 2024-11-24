import random
import time


class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Сума депозиту повинна бути більше нуля")
            return False
        self.balance += amount
        self.transactions.append(f"Депозит: +{amount}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття повинна бути більше нуля")
            return False
        if amount > self.balance:
            print("Недостатньо коштів")
            return False
        self.balance -= amount
        self.transactions.append(f"Зняття: -{amount}")
        return True

    def print_statement(self):
        print(f"Виписка для {self.account_holder}:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Поточний баланс: {self.balance}")


# Менеджер для роботи з багатьма рахунками
class BankManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder):
        if account_holder in self.accounts:
            print("Рахунок вже існує")
            return False
        self.accounts[account_holder] = BankAccount(account_holder)
        print(f"Рахунок створено для {account_holder}")
        return True

    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            print("Відправник або отримувач не існують")
            return False
        if amount <= 0:
            print("Сума переказу повинна бути більше нуля")
            return False
        sender_account = self.accounts[sender]
        receiver_account = self.accounts[receiver]
        if not sender_account.withdraw(amount):
            return False
        receiver_account.deposit(amount)
        print(f"Переказ {amount} від {sender} до {receiver} виконано")
        return True


# Демонстрація роботи
def main():
    bank_manager = BankManager()

    # Створення рахунків
    bank_manager.create_account("Іван")
    bank_manager.create_account("Марія")

    # Випадкові транзакції
    bank_manager.accounts["Іван"].deposit(1000)
    bank_manager.accounts["Марія"].deposit(500)
    bank_manager.accounts["Іван"].withdraw(200)

    # Спроба переказу
    bank_manager.transfer("Іван", "Марія", 300)
    bank_manager.transfer("Іван", "Петро", 100)  # Отримувач не існує

    # Друк виписки
    bank_manager.accounts["Іван"].print_statement()
    bank_manager.accounts["Марія"].print_statement()


# Мертвий код (не використовується, але є в проекті)
def generate_random_account():
    time.sleep(1)  # Затримка для випадковості
    return f"Account_{random.randint(1000, 9999)}"


main()
