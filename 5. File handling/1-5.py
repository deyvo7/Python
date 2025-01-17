# Otwieramy plik 'countries.txt' w trybie do odczytu ('r')
with open('countries.txt', 'r') as file:
    # Inicjalizujemy zmienną 'number', która będzie numerować linie
    number = 1
    
    # Przechodzimy przez każdą linię w pliku
    for line in file:
        # Zmienna 'snumber' tworzy numer w formie stringu, np. "1.", "2.", itd.
        snumber = str(number) + "."
        
        # Drukujemy numer oraz linię z pliku. 'end=""' zapobiega dodaniu dodatkowego nowego wiersza.
        print(snumber, line, end="")
        
        # Zwiększamy 'number' o 1, by następny kraj miał kolejny numer
        number = number + 1
