import threading
import random
import time

class BankAccount:
    def __init__(self, acc_number:str, balance:float = 0.0) -> None:
        self.acc_number:str = acc_number
        self.balance:float = balance
        self.lock = threading.Lock()
    
    def deposit(self,amount:float):
        with self.lock:
            self.balance += amount
            print(f"Account {self.acc_number}: Deposited ${amount}.\nNew Balance: ${self.balance}\n")

    def withdraw(self, amount:float):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Account {self.acc_number}: Withdrew ${amount}.\nNew Balance: ${self.balance}\n")
            else:
                    print(f"Account {self.acc_number}: Withdrawal of ${amount} failed due to insufficient funds.\nCurrent Balance: ${self.balance}\n")

    def balance_check(self):
        print(f"{self.acc_number}'s balance: {self.balance}")

    def transfer_account(self, amount:float, account: object):
        if self.balance >= amount:
            self.balance -= amount
            account.balance += amount
            print(f"Account: {self.acc_number} Transfered ${amount} to Account: {account.acc_number}\n")
        else:
            print(f"Account: {self.acc_number} Transfert of ${amount} to Account: {account.acc_number} failed due to insufficient funds.\nCurrent Balance: ${self.balance}\n")

def simulate_transaction(account1:BankAccount, account2:BankAccount):
    for _ in range(5):  # Perform 5 random transactions
        account = random.choice([account1, account2])
        transaction_type = random.choice(["deposit", "withdrawal"])
        amount = random.randint(10, 100)
        if transaction_type == "deposit":
            account.deposit(amount)
        elif transaction_type == "withdrawal":
            account.withdraw(amount)
        
        time.sleep(random.uniform(2, 6))

def inter_account_transaction(account1:BankAccount, account2:BankAccount):
    for _ in range(5):
        account = random.choice([account1,account2])
        amount = random.randint(10, 100)

        if account == account1:
            account.transfer_account(amount,account2)
        else:
            account.transfer_account(amount,account1)

        time.sleep(random.uniform(2, 6))



if __name__ == "__main__":
    account_01 = BankAccount("Jason")
    account_02 = BankAccount("Ashley")

# Create 5 threads to simulate transactions
threads = []
transaction_threads = []
for i in range(5):
    thread = threading.Thread(target=simulate_transaction, args=(account_01,account_02))
    threads.append(thread)


for i in range(5):
    thread = threading.Thread(target=inter_account_transaction, args=(account_01,account_02))
    transaction_threads.append(thread)

# Start all 5 threads
for thread in threads:
    thread.start()
# Start all 5 threads
for thread in transaction_threads:
    thread.start()


# Wait for all threads to complete
for thread in threads:
    thread.join()
# Wait for all threads to complete
for thread in transaction_threads:
    thread.join()

print(f"Final Balance for Account {account_01.acc_number}: ${account_01.balance}\nFinal Balance for Account {account_02.acc_number}: ${account_02.balance}\n")
