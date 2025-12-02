balance = 0.00

def check_balance():
    print(f"Your balance is: Rs {balance:.2f}")


def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
        print(f"Your balance is: Rs {balance:.2f}")
        deposit_choice = input("Do you want to deposit? (y/n): ")
        if deposit_choice == "y":
            deposit()
        else:
            print("Thank you for using the Noman Rizvi ATM!")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: Rs {balance:.2f}")


def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print(f"Deposit successful. New balance: Rs {balance:.2f}")


def fast_cash():
    global balance
    print("""Please select an option:
    1. 100
    2. 200
    3. 500
    4. 1000
    5. Other""")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = 100
    elif choice == 2:
        amount = 200
    elif choice == 3:
        amount = 500
    elif choice == 4:
        amount = 1000
    elif choice == 5:
        amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: Rs {balance:.2f}")


def main():
    print("Welcome to the Noman Rizvi ATM!")

    while True:
        print("\nPlease select an option:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Fast Cash")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            deposit()
        elif choice == 4:
            fast_cash()
        elif choice == 5:
            print("Thank you for using the Noman Rizvi ATM!")
            break
        else:
            print("Invalid choice. Please try again.")


main()