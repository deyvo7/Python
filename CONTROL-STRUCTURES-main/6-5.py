# The electronic thermometer prints the temperature in degrees Celsius and verbal information according to the following criteria:

# It is extremely hot, for a temperature above 35 degrees,
# It is hot, for a temperature above 30 degrees,
# It is warm, for a temperature of at least 15 degrees,
# It is cold, for a temperature of at least 0 degrees,
# Warning, frost, for a temperature below 0 degrees.
# Write a program that simulates the operation of an electronic thermometer.

# Then check the correctness of the program for the following temperatures in degrees Celsius: 33, 30, 8, 0, -2

###
# Program symulujący działanie elektronicznego termometru
# Program wypisuje komunikaty na podstawie temperatury w stopniach Celsjusza
###

# Przykładowa temperatura
temperature = -2

# Sprawdzanie temperatury i wypisywanie odpowiednich komunikatów
if temperature > 35:
    print("It is extremely hot")  # Bardzo gorąco, jeśli temperatura jest większa niż 35
elif temperature > 30:
    print("It is hot")  # Gorąco, jeśli temperatura jest większa niż 30
elif temperature >= 15:
    print("It is warm")  # Ciepło, jeśli temperatura wynosi co najmniej 15
elif temperature >= 0:
    print("It is cold.")  # Zimno, jeśli temperatura wynosi co najmniej 0
elif temperature < 0: 
    print("Warning, frost")  # Ostrzeżenie, mróz, jeśli temperatura jest poniżej 0
