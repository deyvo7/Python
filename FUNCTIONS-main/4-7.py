# The ICAO (International Civil Aviation Organization) phonetic alphabet is used internationally
# for spelling out letters in radio communication.
# The icao.py program contains a function that returns the corresponding word for a given letter.
# Complete the program to spell out a name entered from the keyboard.

###
# Converts letter to corresponding ICAO word
#
# Funkcja, która zamienia literę na odpowiadające jej słowo w alfabecie fonetycznym ICAO.

def icao(letter):
    # Zamieniamy literę na wielką literę, aby obsłużyć zarówno małe, jak i wielkie litery.
    letter = letter.capitalize()
    
    # Sprawdzamy, jaki jest odpowiednik każdej litery w alfabecie ICAO i przypisujemy do zmiennej 'icao_name'.
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        # Zwracamy '???', jeśli znak nie jest literą alfabetu angielskiego.
        icao_name = '???'

    return icao_name

# Pobieramy imię od użytkownika.
name = input('Enter your name: ')
print('ICAO words for spelling out your name:')

# Iterujemy przez każdą literę w podanym imieniu i wyświetlamy odpowiadające jej słowo ICAO.
for char in name:
    word = icao(char)
    print(word, end=" ")  # Wyświetlamy słowo z oddzieleniem spacji.
