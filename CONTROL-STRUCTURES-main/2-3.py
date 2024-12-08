###
# The car has three driving modes: Auto (A), Manual (M) and Eco (E).
# In each of these three modes, the average fuel consumption in liters
# per 100 km is 7, 9 and 6 respectively. Write a program that calculates
# total fuel consumption for a given distance in km and a given
# driving mode.
#
# Samochód ma trzy tryby jazdy: Auto (A), Manual (M) i Eco (E).
# W każdym z tych trzech trybów średnie zużycie paliwa na 100 km wynosi odpowiednio 7, 9 i 6 litrów.
# Napisz program, który oblicza całkowite zużycie paliwa dla podanej odległości w km oraz
# wybranego trybu jazdy.
###

# Wczytanie trybu jazdy od użytkownika
driving_mode = input('Enter driving mode (A/M/E):')

# Wczytanie odległości w km od użytkownika
distance = int(input('Enter distance in km: '))

# Sprawdzenie trybu jazdy i przypisanie odpowiedniego zużycia paliwa
if driving_mode == 'A':
    fuel_consumption = 7  # litry na 100 km
elif driving_mode == 'M':
    fuel_consumption = 9  # litry na 100 km
elif driving_mode == 'E':
    fuel_consumption = 6  # litry na 100 km

# Obliczenie całkowitego zużycia paliwa
total_consumption = (fuel_consumption / 100) * distance

# Wypisanie wyniku
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:.2f} liters')
