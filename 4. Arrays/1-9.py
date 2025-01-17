# The list contains vehicle registration numbers in Poland.
# Cars from Krakow have numbers starting with the letters 'KR' or 'KK'.
# Write a program that prints car registration numbers from Krakow.
# Number the list printed.

###
# Prints vehicle registration numbers from Krakow
#
# Lista polskich numerów rejestracyjnych
polish_license_plates = [
    'KR5233F', 'PO6987E', 'KR16179', 'BI7192L', 'KK12255',
    'WA7930T', 'SK6922I', 'KK61108', 'KR90538', 'BI8052Q',
    'KK54985', 'LU4864U'
]

# Inicjujemy licznik numeracji
counter = 1

# Przechodzimy przez listę numerów rejestracyjnych
for car_number in polish_license_plates:
    # Sprawdzamy, czy numer zaczyna się od "KR" lub "KK"
    if car_number[:2] == "KR" or car_number[:2] == "KK":
        # Wypisujemy numer listy i numer rejestracyjny
        print(f"{counter}. {car_number}")
        counter += 1  # Zwiększamy licznik
