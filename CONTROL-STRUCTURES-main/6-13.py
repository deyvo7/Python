# The speed of vehicles on highways in Poland is at least 40 km/h and not more than 140 km/h. 
# Write a program that prints a message when the specified car speed, read from the keyboard, has been exceeded.
# Sample result:

# Enter car speed: 38
# Warning: invalid car speed!!

# Use the following variables in your program:

# car_speed
# speed_limit_min
# speed_limit_max

# Minimalna i maksymalna dozwolona prędkość na autostradach w Polsce
speed_limit_min = 40  # Minimalna prędkość (40 km/h)
speed_limit_max = 140  # Maksymalna prędkość (140 km/h)

# Wprowadzenie prędkości samochodu
car_speed = int(input("Enter car speed (km/h): "))

# Sprawdzenie, czy prędkość samochodu mieści się w dozwolonym zakresie
if car_speed >= 40 and car_speed <= 140:
    print("The car speed is fine.")  # Prędkość jest w porządku
else:
    print("Warning: invalid car speed!!")  # Przekroczono dozwoloną prędkość
