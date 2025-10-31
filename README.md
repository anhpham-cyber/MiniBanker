# MiniBanker - Simple Online Banking System

MiniBanker is a simple Python program that simulates an online banking system.  
It allows users to **create accounts, deposit and withdraw money, transfer funds, and view account balances**.  
This project is designed to practice **Python functions, loops, input validation, and dictionary data management**.

---

## Features

- **Create new accounts** with a custom account name and opening balance  
- **Deposit money** into existing accounts  
- **Withdraw money** with balance checks to prevent overdrafts  
- **Transfer money** between accounts with validation  
- **View all accounts** and their current balances  
- Simple **text-based console menu** for easy navigation  

---

## Example Menu

Menu

Create a new account

Deposit money

Withdraw money

Transfer money to another account

View all accounts

Exit

Please select an option (1-6):

---

## Example Workflow

Create your account name: Alice

Enter your opening balance: 500

Account 'Alice' has been created. Opening balance: $500


Please enter your account name: Alice

How much would you like to deposit today: $200

Successfully deposited $200 in 'Alice' Account!


Please enter your account name: Alice

Enter the amount you would like to withdraw today: $100

Successfully withdrew $100, from 'Alice' Account!

Please select an option: 5

----------View all Accounts----------

Account 1. Account name: 'Alice'. Account Balance: $600

---

## Requirements

- Python 3.x
- No external libraries required

---

## Notes

- All inputs are validated to prevent errors (e.g., negative balances, invalid account names).

- This program is a text-based simulation for learning purposes and is not connected to real banking systems.

- You can easily extend it to include file-based storage, transaction history, or a graphical interface in the future.

