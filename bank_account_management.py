print(" WELCOME TO PYTHON BANK: ")

customer_name = input("Enter customer name: ")
account_number = input("Enter account number: ")

initial_balance = float(input("Enter initial balance: "))
deposit_amount = float(input("Enter deposit amount: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

account_active = True

total_balance = initial_balance + deposit_amount - withdrawal_amount

print("\n ACCOUNT SUMMARY :")
print("Customer Name   :", customer_name)
print("Account Number  :", account_number)
print("Initial Balance :", initial_balance)
print("Deposit Amount  :", deposit_amount)
print("Withdrawal      :", withdrawal_amount)
print("-------------------------------------")
print("Available Balance:", round(total_balance, 2))
print("Account Active  :", account_active)
print("=======================================")
