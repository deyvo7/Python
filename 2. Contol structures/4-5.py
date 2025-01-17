###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
###
# Szyfrowanie tekstu za pomocą kodu Cezara, przesuwając każdą literę
# w alfabecie o jedną pozycję w prawo
###

# Tekst do zaszyfrowania
plain_text = 'The early bird catches the worm'  

# Zmienna do przechowywania zaszyfrowanego tekstu
encrypted_text = ''

# Pętla przechodząca przez każdy znak w tekście
for char in plain_text:
    if char.isalpha():  # Sprawdź, czy znak jest literą
        if char.islower():  # Jeśli to mała litera
            new_char_code = ord(char) + 1  # Zwiększ kod ASCII o 1
            if new_char_code > ord('z'):  # Jeśli wyjdzie poza 'z', wróć do 'a'
                new_char_code -= 26
        elif char.isupper():  # Jeśli to wielka litera
            new_char_code = ord(char) + 1  # Zwiększ kod ASCII o 1
            if new_char_code > ord('Z'):  # Jeśli wyjdzie poza 'Z', wróć do 'A'
                new_char_code -= 26
        
        encrypted_char = chr(new_char_code)  # Zamień kod ASCII z powrotem na znak
        encrypted_text += encrypted_char  # Dodaj zaszyfrowany znak do wyniku
    else:
        encrypted_text += char  # Jeśli to nie litera, pozostaw znak bez zmian

# Wyświetl teksty
print("Plain text:", plain_text)  # Oryginalny tekst
print("Encrypted text:", encrypted_text)  # Zaszyfrowany tekst
