
# show balance
def show_balance(balance):
    print(f"Your balance is Rs.{balance:.2f}")

# deposit amount
def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return 0
        return amount
    except ValueError:
        print("Invalid input!")
        return 0

# withdraw amount
def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
            return 0
        elif amount <= 0:
            print("Amount must be greater than 0.")
            return 0
        return amount
    except ValueError:
        print("Invalid input!")
        return 0

# PIN verification
def verify_pin():
    CORRECT_PIN = "1234"
    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin == CORRECT_PIN:
            print("PIN verified successfully ✅")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")

    print("Account locked ❌")
    return False

# main function
def main():
    if not verify_pin():
        return

    balance = 0.0

    while True:
        print("\n******** Banking Program ********")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid choice!")
            continue

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("Thank you! Have a nice day 😊")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()


