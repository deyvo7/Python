# Define a function that returns the full name of a day of the week based on its number.
###
# Function that returns the full name of a day of the week
# based on its number
#
# Definiujemy funkcję, która zwraca pełną nazwę dnia tygodnia na podstawie jego numeru.

def day_name(day_number):
    # Inicjalizujemy zmienną 'result', która będzie przechowywać nazwę dnia.
    result = ''
    
    # Sprawdzamy numer dnia i przypisujemy odpowiednią nazwę dnia do zmiennej 'result'.
    if day_number == 1:
        result = 'Monday'  # Poniedziałek
    elif day_number == 2:
        result = 'Tuesday'  # Wtorek
    elif day_number == 3:
        result = 'Wednesday'  # Środa
    elif day_number == 4:
        result = 'Thursday'  # Czwartek
    elif day_number == 5:
        result = 'Friday'  # Piątek
    elif day_number == 6:
        result = 'Saturday'  # Sobota
    elif day_number == 7:
        result = 'Sunday'  # Niedziela
    
    # Zwracamy nazwę dnia tygodnia.
    return result

# Przykład użycia funkcji.
# Wywołujemy funkcję i wyświetlamy wynik dla dni o numerach 5, 3 i 7.
print('The name of day 5 in the week is', day_name(5))  # Oczekiwany wynik: 'Friday'
print('The name of day 3 in the week is', day_name(3))  # Oczekiwany wynik: 'Wednesday'
print('The name of day 7 in the week is', day_name(7))  # Oczekiwany wynik: 'Sunday'
