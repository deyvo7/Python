###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
# Oblicza i wypisuje kwartał roku dla podanego numeru miesiąca (1..12)

# Wczytanie numeru miesiąca od użytkownika
month = int(input('Enter month number (1..12): '))

# Określenie, do którego kwartału należy podany miesiąc
if month >= 10:
    quarter = 4  # Miesiące 10, 11, 12 są w czwartym kwartale
elif month >= 7:
    quarter = 3  # Miesiące 7, 8, 9 są w trzecim kwartale
elif month >= 4:
    quarter = 2  # Miesiące 4, 5, 6 są w drugim kwartale
elif month >= 1:
    quarter = 1  # Miesiące 1, 2, 3 są w pierwszym kwartale

# Wypisanie wyniku
print(f'Month {month} is in quarter {quarter}')
