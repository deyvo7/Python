###
# ATM (cash machine) simulator

balance = 1000  # Initial balance
pin = '1111'    # initial 4-digit PIN code

# ATM function loop
while True:
    print()  # Print empty line for better readability
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # User choice input
    choice = input("Choose an option (1-4): ")
    print()  # Print empty line after input choice

    # Checking balance
    if choice == '1':
        print(f"Your current balance is: €{balance}")
    
    # Deposit money
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    
    # Withdraw money
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    
    # Exit the program
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop and end the program
    
    # Handle invalid option
    else:
        print("Invalid option. Please try again.")
