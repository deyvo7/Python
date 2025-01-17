###
# Funkcje do wczytywania danych różnych typów z klawiatury
###

# Funkcja do wczytywania ciągu znaków (string)
def input_string(message):
    # Wczytaj ciąg znaków od użytkownika
    string = str(input(message))
    return string

# Funkcja do wczytywania liczby całkowitej (integer)
def input_integer(message):
    # Wczytaj liczbę całkowitą od użytkownika
    integer = int(input(message))
    return integer

# Funkcja do wczytywania liczby rzeczywistej (float)
def input_real(message):
    # Wczytaj liczbę rzeczywistą od użytkownika
    real = float(input(message))
    return real

# Funkcja do wczytywania wartości logicznej (boolean)
def input_boolean(message):
    # Wczytaj wartość od użytkownika jako ciąg znaków
    boolean_con = str(input(message))
    # Jeśli użytkownik wprowadzi "y" (tak), zwróć True
    if boolean_con.lower() == "y":
        return True
    # Jeśli użytkownik wprowadzi "n" (nie), zwróć False
    elif boolean_con.lower() == "n":
        return False
