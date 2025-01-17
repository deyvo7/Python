# Define the function f(n), which returns numbers from 1 to n as a string. Sample result:

# f(11) returns "1234567891011"
# f(4) returns "1234"

# Funkcja zwracająca ciąg liczb od 1 do n jako jeden ciąg znaków
def f(n):
    result = ""  # Inicjalizacja pustego ciągu znaków
    for i in range(1, n + 1):  # Pętla przechodząca od 1 do n (włącznie)
        result += str(i)  # Dodanie liczby i do ciągu result jako ciągu znaków
    return result  # Zwracamy wynik

# Testowanie funkcji
print(f(11))  # Powinno zwrócić "1234567891011"
print(f(4))   # Powinno zwrócić "1234"
