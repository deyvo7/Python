# Write a program that calculates, prints, and saves to a text file integers from 1 to 100 and their second and third powers.

# Sample result:
# 1,1,1
# 2,4,8
# 3,9,27
# ...
# ...

# Nazwa pliku, do którego zapisujemy wyniki
output_file = 'powers.txt'

# Otwieramy plik w trybie zapisu ('w' - write), jeśli plik nie istnieje, zostanie utworzony
with open(output_file, 'w') as file:
    # Pętla iterująca przez liczby od 1 do 100
    for i in range(1, 101):
        # Obliczamy drugą i trzecią potęgę liczby i
        second_power = i ** 2
        third_power = i ** 3

        # Tworzymy ciąg znaków w formacie "i,second_power,third_power"
        line = f"{i},{second_power},{third_power}\n"

        # Zapisujemy ciąg do pliku
        file.write(line)

# Informujemy użytkownika, że dane zostały zapisane
print("Dane zostały zapisane do pliku 'powers.txt'.")
