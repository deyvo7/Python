# The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

###
# Program obliczający opłatę za parking w zależności od liczby godzin
# Zasady: 
# 1-2 godziny: 5 PLN
# 3-6 godzin: 15 PLN
# Powyżej 6 godzin: 20 PLN
###

# Pobieranie liczby godzin parkowania od użytkownika
parking_time = int(input("Enter the parking time (in hours): "))

# Sprawdzanie, jaki jest czas parkowania i przypisywanie odpowiedniej opłaty
if parking_time > 6:
    print("The fee is 20 PLN")  # Opłata wynosi 20 PLN, jeśli czas parkowania przekracza 6 godzin
elif parking_time >= 3:
    print("The fee is 15 PLN")  # Opłata wynosi 15 PLN, jeśli czas parkowania wynosi od 3 do 6 godzin
elif parking_time >= 1:
    print("The fee is 5 PLN")  # Opłata wynosi 5 PLN, jeśli czas parkowania wynosi od 1 do 2 godzin
