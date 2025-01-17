###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
###
# Program, który oblicza wynagrodzenie pracownika,
# uwzględniając możliwość otrzymania premii.
###

# Podstawowe wynagrodzenie pracownika
basic_salary = 5000

# Całkowite wynagrodzenie po uwzględnieniu premii
total_salary = 0

# Zmienna określająca, czy pracownik otrzymuje premię
is_bonus = input('Does employee receive a bonus? (Y/N): ') == 'Y'  # Czy pracownik otrzymuje premię
bonus = 0.15  # Wysokość premii (15%)

# Sprawdzenie, czy pracownik otrzymuje premię
if is_bonus:
    # Obliczenie wynagrodzenia z uwzględnieniem premii
    total_salary = basic_salary + bonus * 2 * basic_salary
else:
    # Jeśli nie ma premii, całkowite wynagrodzenie to tylko wynagrodzenie podstawowe
    total_salary = basic_salary

# Wyświetlenie szczegółowych informacji o wynagrodzeniu
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')
