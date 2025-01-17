# The vowels.py program counts vowels in the text. Modify the program. Replace the 'for' statement with a 'while' statement.

###
# Counts vowels in the text
#
###
# Liczy samogłoski w tekście
###

# Tekst, w którym będą liczone samogłoski
text = "This is a sample text."  
# Zbiór samogłosk (małe i duże litery)
vowels = "aeiouAEIOU"  
# Zmienna do przechowywania liczby samogłosk
vowel_count = 0  
# Indeks do iteracji po tekście
index = 0  

# Pętla while, która przechodzi przez wszystkie znaki w tekście
while index < len(text):
    # Sprawdza, czy dany znak jest samogłoską
    if text[index] in vowels:
        vowel_count += 1  # Jeśli jest, zwiększa licznik samogłosk
    index += 1  # Zwiększa indeks, aby przejść do następnego znaku

# Wyświetla wynik - liczbę samogłosk
print(f"The number of vowels in the text is: {vowel_count}")
