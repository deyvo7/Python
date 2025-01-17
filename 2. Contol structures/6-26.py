# The payment card is secured with a four-digit PIN code (0805).
# Write a program that checks if the PIN code entered in the payment terminal is correct.
# The user has up to three possibilities for entering a PIN code. In case of three unsuccessful attempts, the card is blocked.

# Sample result:
# Enter the PIN code: 2398
# Incorrect...
# Enter the PIN code: 0912
# Incorrect...
# Enter the PIN code: 7860
# Incorrect...
# Sorry, your payment card has been blocked.

# Program, który sprawdza poprawność kodu PIN i blokuje kartę po trzech nieudanych próbach

correct_pin = "0805"  # Poprawny kod PIN
attempts = 3  # Maksymalna liczba prób

for attempt in range(attempts):  # Pętla dla prób
    pin = input("Enter the PIN code: ")  # Wczytaj kod PIN od użytkownika
    if pin == correct_pin:  # Jeśli kod PIN jest poprawny
        print("Access granted.")  # Przyznaj dostęp
        break  # Zakończ pętlę
    else:
        print("Incorrect...")  # Jeśli kod PIN jest niepoprawny

else:  # Jeśli pętla zakończy się bez przerwania (po trzech próbach)
    print("Sorry, your payment card has been blocked.")  # Zablokowanie karty
