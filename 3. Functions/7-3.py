# Each month of a calendar year can be expressed by its name or by a number that indicates the position of the month in year.
# In a separate module, define a function month(n) that returns a month name based on the month number (values from 1 to 12).
# Then, write a program to print the name of the month 7. Import the module with the created function. Sample result:

# Enter month number: 9
# The name of month 9 is September


# Importowanie funkcji month z modułu module_7_3
from module_7_3 import month

def main():
    # Pobranie numeru miesiąca od użytkownika
    month_number = int(input("Wprowadź numer miesiąca: "))
    # Wywołanie funkcji, aby uzyskać nazwę miesiąca
    month_name = month(month_number)
    # Wyświetlenie wyniku
    print(f"Nazwa miesiąca {month_number} to {month_name}")

# Upewnienie się, że skrypt działa tylko wtedy, gdy jest głównym programem
if __name__ == "__main__":
    main()
