# The weather station measures temperature once a day.
# The measurement results for each day in March are stored in an array.
# Write a program that analyzes the temperature based on the
# observations from March and prints the following report:

# TEMPERATURE REPORT
# Month: March
# Number of measurements:
# Average temperature in the month:
# Minimum temperature:
# Maximum temperature:
# Number of days with negative temperature:

###
# The weather station report
#
# Wyniki pomiarów temperatur w marcu (1 pomiar dziennie)
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# Liczba pomiarów
measurements = len(temperatures)

# Obliczanie średniej temperatury
total_temp = 0
for temp in temperatures:  # Iterujemy przez każdą temperaturę
    total_temp += temp  # Dodajemy temperaturę do sumy

avg_temp = total_temp / measurements  # Średnia temperatura

# Najniższa i najwyższa temperatura
min_temp = min(temperatures)  # Minimalna temperatura
max_temp = max(temperatures)  # Maksymalna temperatura

# Liczba dni z temperaturą ujemną
negative_temp = 0
for temp in temperatures:  # Iterujemy przez temperatury
    if temp < 0:  # Sprawdzamy, czy temperatura jest ujemna
        negative_temp += 1  # Zwiększamy licznik dni z ujemną temperaturą

# Wyświetlanie raportu
print("TEMPERATURE REPORT")
print("Month: March")
print("Number of measurements:", measurements)
print("Average temperature in the month:", round(avg_temp, 2))  # Zaokrąglamy średnią do 2 miejsc
print("Minimum temperature:", min_temp)
print("Maximum temperature:", max_temp)
print("Number of days with negative temperature:", negative_temp)
