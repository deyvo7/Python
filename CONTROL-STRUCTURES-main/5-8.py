# The atm.py program simulates a simple ATM where the user can deposit, withdraw, or check the balance.
# Analyze the program code and then run the program. Next, add two more functions to the program:

# Check PIN
# Change PIN
# The PIN should consist of exactly 4 digits.
# To check if a string contains only digits, you can use the isdigit() method.
# This method returns True if all characters in the string are digits and False otherwise:
# https://www.geeksforgeeks.org/python-string-isdigit-method/

###
# ATM (cash machine) simulator
###
# Symulator bankomatu (ATM), który umożliwia sprawdzenie salda, wpłatę, wypłatę, zmianę PINu
# Program teraz posiada również możliwość sprawdzenia PINu oraz zmiany PINu
###

# Początkowy stan konta
balance = 1000  # Initial balance
# Początkowy PIN
pin = '1111'  # initial 4-digit PIN code

# Wprowadzenie PINu przez użytkownika
entered_pin = input("Enter your pin: ")

# Sprawdzenie, czy PIN składa się tylko z cyfr i czy jest poprawny
is_digit = entered_pin.isdigit()
if is_digit == True and entered_pin == pin:
    while True:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change your pin")
        print("5. Check pin")
        print("6. Exit")

        # Wybór opcji przez użytkownika
        choice = input("Choose an option (1-6): ")
        print()

        if choice == '1':
            # Wyświetlenie salda
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            # Wpłata pieniędzy
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            # Wypłata pieniędzy
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            # Zmiana PINu
            entered_pin = input("Enter your old pin: ")
            if entered_pin == pin:
                while True:
                    entered_pin = input("Enter your new pin code (it should consist of 4 digits): ")
                    if entered_pin.isdigit() and len(entered_pin) == 4:
                        pin = entered_pin
                        print(f"Your pin is now: {pin}")
                        break
                    else:
                        print("Incorrect pin.")
            else:
                print("Incorrect pin")
        elif choice == '5':
            # Sprawdzenie PINu
            entered_pin_check = input("Enter your pin to check: ")
            if entered_pin_check == pin:
                print("Your pin is correct.")
            else:
                print("Incorrect pin")
        elif choice == '6':
            # Wyjście z programu
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop
        else:
            # Błędny wybór
            print("Invalid option. Please try again.")
else:
    # Błędny PIN
    print("Incorrect pin")
