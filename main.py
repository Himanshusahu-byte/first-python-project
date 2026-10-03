Account_number = "123456789"
pin = "1234"
balance = 10000
transactions = []

    # Login System.

def login():
    print("\nATM Login ")

    entered_account = input("Enter Your Account Number: ")

    if entered_account == Account_number:
        print(" ")
    else:
        print("Invalid Account Number ")
        return False
       
    entered_pin = input("Enter Your PIN: ")

    if entered_pin == pin:
        return True
    else:
        print("Invalid PIN ")
        return False

    # Balance Check

def check_balance():
    print("\n YOUR CHOICE IS 1. CHECK BALANCE ")
    print("Your current balance is: $", balance)

     # Money Deposite

def deposit_money():
    global balance

    print("\n YOUR CHOICE IS 2. DEPOSIT MONEY ")

    amount = float(input("Enter amount to deposit: $"))

    if amount > 0:
        balance = balance + amount

        transactions.append("Deposited $" + str(amount))

        print("Money deposited successfully.")
        print("New balance: $", balance)

    else:
        print("Please enter a valid amount.")

    # Money Withdrawl

def withdraw_money():
    global balance

    print("\n YOUR CHOICE IS 3. WITHDRAW MONEY ")

    amount = float(input("Enter amount to withdraw: $"))

    if amount <= 0:
        print("Please enter a valid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance = balance - amount

        transactions.append("Withdrawn $" + str(amount))

        print("Please collect your cash.")
        print("Remaining balance: $", balance)

      # Statement

def mini_statement():
    print("\n YOUR CHOICE IS 4. MINI STATEMENT ")

    if len(transactions) == 0:
        print("No transactions yet.")

    else:
        print("Transaction History:")

        for transaction in transactions:
            print("-", transaction)

    print("Current Balance: $", balance)

      # PIN Change 

def change_pin():
    global pin

    print("\n YOUR CHOICE IS 5. CHANGE PIN ")

    old_pin = input("Enter your current PIN: ")

    if old_pin == pin:

        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")

        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully.")

        else:
            print("New PIN and confirmation PIN do not match.")

    else:
        print("Incorrect current PIN.")

   # ATM Menu
      
def atm_menu():
    while True:
        print("\n WELCOME TO IPS-IPS BANK ")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            mini_statement()
        elif choice == "5":
            change_pin()
        elif choice == "6":
            print("\nThank you for using IPS-IES Bank ATM.")
            print("Please take your card.")
            break
        else:
            print("Invalid choice. Please select 1-6.")

print("\n IPS-IES BANK.")

if login():
    atm_menu()
else:
    print(" ")
