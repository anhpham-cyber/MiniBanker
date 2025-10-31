
def create_account(account: dict) -> None:
    while True:
        name = input("Create your account name: ").strip().title()
        if not name:
            print("Account name cannot be empty!")
        if name in account:
            print(f"Account '{name}' already exist!")
        else:
            break
    while True:
        balance = input("Enter your opening balance: ").strip()
        if balance.isdigit():
            balance = int(balance)
            break
        else:
            print("Opening balance must be a number! ")
    account[name] = balance
    print(f"Account '{name}' has been created. Opening balance: ${balance}")
        

def account_deposit(account: dict) -> None:
    while True:
        name = input("Please enter your account name: ").strip().title()
        if name not in account:
            print(f"{name} is not found in the system!")
            return
        else:
            break

    while True:
        deposit = input("How much would you like to deposit today: $").strip()
        if deposit.isdigit():
            deposit = int(deposit)
            break
        else:
            print(f"{deposit} is an invalid input. Please enter the positive number!")
    account[name] += deposit
    print(f"\nSuccessfully deposited ${deposit} in '{name}' Account!\n")

def check_fund(account: dict, name: str, amount: int) -> bool:
    if amount > account[name]:
        return False
    return True

def withdraw(account: dict, name: str):
    while True:
        if name not in account:
            print(f"{name} is not found in the system!")
            return
        else:
            break
    while True:
        amount = input("Enter the amount you would like to withdraw today: $")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print(f"{amount} is an invalid input. You must entering a number!")
    if check_fund(account, name, amount):
        account[name] -= amount
        print(f"Successfully withdrew ${amount}, from '{name}' Account!")
    else:
        print(f"Withdrawal failed due to insufficient funds.")

def transfer(account: dict):
    print("------------------Transfer money processing------------------")
    while True:
        account1 = input("Please enter the account you would like to withdraw the money: ").strip().title()
        if account1 not in account:
            print(f"{account1} is not found in the system!")
            return
        else:
            break
    
    while True:
        amount = input("Enter the amount you would like to transfer today: $")
        if amount.isdigit():
            amount = int(amount)
            break
        else:
            print(f"{amount} is an invalid input. Transfer amount must be a positive number!")
    
    while True:
        account2 = input("Please enter the account you would like to deposit the money: ").strip().title()
        if account2 not in account:
            print(f"{account2} is not found in the system!")
            return
        else:
            break

    if account[account1] >= amount:
        account[account1] -= amount
        account[account2] += amount
        print("Transfer successfull!")
        for name, balance in account.items():
            print(f"Account: {name}. Balance: ${balance}")
    else:
        print("Not enough balance to transfer!")
        for name, balance in account.items():
            print(f"Account: {name}. Balance: ${balance}")


def view_account(account: dict) -> None:
    if not account:
        print("No account in online banking system")
        return
    print("\n----------View all Accounts----------")
    for i, (name, balance) in enumerate(account.items(), start=1):
        print(f"Account {i}. Account name: '{name}'. Account Balance: ${balance}")
    print("-------------------------------------")

def main():
    account = {}

    print("---------------------------------")
    print("Welcome to online banking system.")
    print("---------------------------------")

    while True:
        print("\nMenu")
        print("1. Create a new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Trasfer money to another account")
        print("5. View all accounts")
        print("6. Exit")
        
        select = input("Please select an option (1-6): ")
        if select == "1":
            create_account(account)
        elif select == "2":
            account_deposit(account)
        elif select == "3":
            name = input("Please enter your account name: ").strip().title()
            withdraw(account, name)
        elif select == "4":
            transfer(account)
        elif select == "5":
            view_account(account)
        elif select == "6":
            print("---------------------------------------------------")
            print("Thank you for using online banking system. Goodbye!")
            print("---------------------------------------------------")
            break
        else:
            print(f"{select} is an invalid input. Please select an option between 1-6!")

if __name__ == "__main__":
    main()
