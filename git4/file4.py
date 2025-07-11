balance = 1000

def check_balance():
    print(f"Your current balance is: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited.")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Please collect your cash.")
    else:
        print("Insufficient balance!")

while True:
    print("\nATM Menu\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    option = input("Select option: ")
    if option == '1':
        check_balance()
    elif option == '2':
        deposit()
    elif option == '3':
        withdraw()
    elif option == '4':
        print("Thank you! Visit again.")
        break
    else:
        print("Invalid choice.")

