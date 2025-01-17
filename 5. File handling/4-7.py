# Write a program that calculates the number of vowels in the text entered from the keyboard. Use regular expressions.

import re  # Importujemy moduł do pracy z wyrażeniami regularnymi

# Funkcja do liczenia samogłosk w tekście
def count_vowels(text):
    # Wyrażenie regularne do wyszukiwania samogłosk (małe i wielkie litery)
    pattern = r'[aeiouAEIOU]'  # 'a, e, i, o, u' oraz ich wielkie odpowiedniki
    vowels = re.findall(pattern, text)  # findall() zwróci listę wszystkich samogłosk
    return len(vowels)  # Zwracamy liczbę znalezionych samogłosk

# Pobieramy tekst od użytkownika
text = input("Wprowadź tekst: ")

# Liczymy samogłoski w wprowadzonym tekście
vowels_count = count_vowels(text)

# Wyświetlamy wynik
print(f"Liczba samogłosk w wprowadzonym tekście: {vowels_count}")
