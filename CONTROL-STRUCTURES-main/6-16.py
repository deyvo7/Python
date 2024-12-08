# A washing machine allows you to wash a jacket, which takes 40 minutes, wash underwear, which takes 70 minutes,
# and wash shoes, which takes 20 minutes. In addition, it is possible to program an additional rinse (15 minutes)
#  and an additional spin (9 minutes). The washing machine settings are saved in variables.
# Write a program that calculates and prints the total washing time.

# Sample result:
# washing_product = "shoes"
# rinse = True
# spin = False
# Total washing time: 35 minutes

# Program obliczający całkowity czas prania w zależności od wybranego produktu i dodatkowych opcji

# Inicjalizacja zmiennej przechowującej czas prania
washing_time = 0

# Pobranie danych o produkcie, który ma zostać prany
washing_product = input("Enter the washing product (jacket/underwear/shoes): ")

# Określenie czasu prania w zależności od wybranego produktu
if washing_product.lower() == "jacket":
    washing_time += 40  # Czas prania kurtki (40 minut)
elif washing_product.lower() == "underwear":
    washing_time += 70  # Czas prania bielizny (70 minut)
elif washing_product.lower() == "shoes":
    washing_time += 20  # Czas prania butów (20 minut)

# Pobranie danych o dodatkowych opcjach (płukanie i wirowanie)
rinse = input("Additional rinse? (yes/no): ")
spin = input("Additional spin? (yes/no): ")

# Sprawdzenie, czy użytkownik wybrał dodatkowe płukanie
if rinse.lower() == "yes":
    washing_time += 15  # Czas dodatkowego płukania (15 minut)

# Sprawdzenie, czy użytkownik wybrał dodatkowe wirowanie
if spin.lower() == "yes":
    washing_time += 9  # Czas dodatkowego wirowania (9 minut)

# Wyświetlenie całkowitego czasu prania
print("Total washing time: ", washing_time)
