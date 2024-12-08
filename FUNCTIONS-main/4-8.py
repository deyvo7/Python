# Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23)
# and the number of minutes (0..59), returns a string specifying the time in the given format
# ('24' for 24-hour time and '12' for 12-hour time).

# Then write a program that tests whether the function works correctly.

# time_string(15, 38, '24') returns '15:38'
# time_string(8, 3, '24') returns '08:03'
# time_string(0, 5 '24') returns '00:05'
# time_string(11, 15, '12') returns '11:15am'
# time_string(0, 7, '12') returns '12:07am'
# time_string(7, 30, '12') returns '7:30am'
# time_string(12, 46, '12') returns '12:46pm'
# time_string(13, 10, '12') returns '1:10pm'
# time_string(19, 02, '12') returns '7:02pm'
# Hint: Use f-strings formatting. Search the Internet for 'Format numbers using f-strings'.
# Funkcja, która zwraca czas w określonym formacie (12-godzinnym lub 24-godzinnym).

def time_string(hours, minutes, time_format):
    result = ''  # Zmienna do przechowywania końcowego wyniku.

    # Sprawdzamy, czy format to 12-godzinny.
    if time_format == '12':
        # Sprawdzamy, czy godziny są większe niż 12 (czyli po południu).
        if hours > 12:
            pm_hours = hours - 12  # Obliczamy godzinę w formacie 12-godzinnym.
            str_hours = str(pm_hours)  # Konwertujemy godzinę na napis.
        # Sprawdzamy, czy godzina jest równa lub mniejsza od 12, ale nie jest zerem.
        elif hours <= 12 and hours != 0:
            str_hours = str(hours)
        # Jeśli godzina jest równa 0 (północ), zmieniamy ją na 12.
        elif hours == 0:
            hours = hours + 12
            str_hours = str(hours)
        
        # Sprawdzamy, czy liczba minut jest mniejsza niż 10 (dodajemy wiodącą zerówkę).
        if minutes < 10:
            str_minutes = str(minutes)
            str_minutes = "0" + str_minutes
        else:
            str_minutes = str(minutes)

        # Dodajemy odpowiedni sufiks 'am' lub 'pm' do godziny.
        if hours >= 12:
            result = str_hours + ":" + str_minutes + "pm"
        else:
            result = str_hours + ":" + str_minutes + "am"
    
    # Sprawdzamy, czy format to 24-godzinny.
    elif time_format == '24':
        str_hours = str(hours)
        # Dodajemy wiodącą zerówkę do minut, jeśli są mniejsze niż 10.
        if minutes < 10:
            str_minutes = str(minutes)
            str_minutes = "0" + str_minutes
        else:
            str_minutes = str(minutes)
        
        # Łączymy godziny i minuty w formacie 24-godzinnym.
        result = str_hours + ":" + str_minutes
    
    # Zwracamy sformatowany czas.
    return result

# Testowanie funkcji z różnymi przypadkami.
print(time_string(15, 38, '24'))   # Powinno zwrócić '15:38'
print(time_string(8, 3, '24'))     # Powinno zwrócić '08:03'
print(time_string(0, 5, '24'))     # Powinno zwrócić '00:05'
print(time_string(11, 15, '12'))   # Powinno zwrócić '11:15am'
print(time_string(0, 7, '12'))     # Powinno zwrócić '12:07am'
print(time_string(7, 30, '12'))    # Powinno zwrócić '7:30am'
print(time_string(12, 46, '12'))   # Powinno zwrócić '12:46pm'
print(time_string(13, 10, '12'))   # Powinno zwrócić '1:10pm'
print(time_string(19, 2, '12'))    # Powinno zwrócić '7:02pm'
