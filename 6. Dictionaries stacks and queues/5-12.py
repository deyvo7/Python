# Funkcja odwracająca tekst za pomocą stosu
def reverse_string(text):
    stack = []  # Tworzymy pusty stos
    # Dodajemy każdy znak tekstu na stos
    for char in text:
        stack.append(char)
    
    reversed_text = ""  # Zmienna do przechowywania odwróconego tekstu
    # Usuwamy znaki ze stosu i tworzymy nowy odwrócony tekst
    while stack:
        reversed_text += stack.pop()  # Zdejmujemy element ze stosu i dodajemy go do odwróconego tekstu
    
    return reversed_text

# Program główny
text = input("Wpisz tekst do odwrócenia: ")  # Pobieramy tekst od użytkownika
reversed_text = reverse_string(text)  # Wywołujemy funkcję do odwrócenia tekstu
print("Odwrócony tekst:", reversed_text)  # Wyświetlamy wynik
