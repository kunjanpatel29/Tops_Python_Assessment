# Write a program to demonstrate the bank management Console based application.

# Create Bank Class
class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

# Create Account Class
class Account:
    def __init__(self, number, cname, balance):
        self.number = number
        self.cname = cname
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(amount, 'Deposit'))

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(Transaction(amount, 'Withdrawal'))
        else:
            print('Insufficient funds')

    def check_balance(self,balance):
        print("Your Cureent Balance is : ",self.balance)

# Transaction Class
class Transaction:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

# Main Function 
def main():
    print("WELCOME TO PYTHON BANK MANAGEMENT SYSTEM\n")

    bank_name = input('Enter Bank Name: ')
    bank = Bank(bank_name)
    print('\nBank', bank_name, 'Created Successfully')
    while True:
        print('\n\t\t 1.Create Account')
        print('\t\t 2.Deposit')
        print('\t\t 3.Withdraw')
        print('\t\t 4.Check Balance')
        print('\t\t 5.Exit')

        choice = int(input('Enter your choice(1-5): '))

        if choice == 1:
            ac_no = input('Enter account number: ')
            cname = input('Enter Customer name: ')
            balance = float(input('Enter opening balance: '))
            account = Account(ac_no, cname, balance)
            bank.add_account(account)
            print('\nAccount created successfully')

        elif choice == 2:
            ac_no = input('Enter account number: ')
            amount = float(input('Enter amount to deposit: '))
            account = find_account(bank.accounts, ac_no)
            if account:
                account.deposit(amount)
                print('Deposit successful')
            else:
                print('Account not found')

        elif choice == 3:
            ac_no = input('Enter account number: ')
            amount = float(input('Enter amount to withdraw: '))
            account = find_account(bank.accounts, ac_no)
            if account:
                account.withdraw(amount)
                print('Withdrawal successful')
            else:
                print('Account not found')

        elif choice == 4:
            account.check_balance(balance)

        elif choice == 5:
            print('Thank you for using the Bank Management System')
            break

        else:
            print('Invalid choice')

# Function For find Account
def find_account(accounts, number):
    for account in accounts:
        if account.number == number:
            return account
    return None

if __name__ == '__main__':
    main()
