###
# Checks if the given day number of the month is correct
#
###
# Sprawdza, czy podany numer dnia miesiąca jest poprawny
###

# Pobierz numer miesiąca od użytkownika
month = int(input('Enter month number (1..12): '))  # Wprowadź numer miesiąca (od 1 do 12)

# Pobierz numer dnia od użytkownika
day = int(input('Enter the day number of the month: '))  # Wprowadź numer dnia w miesiącu

# Inicjalizuj zmienną, która przechowuje informację, czy dzień jest poprawny
day_ok = False  # Na początku zakładamy, że dzień jest niepoprawny

# Sprawdź, ile dni ma dany miesiąc
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    # Miesiące z 31 dniami: styczeń, marzec, maj, lipiec, sierpień, październik, grudzień
    if day >= 1 and day <= 31:  
        day_ok = True  # Jeśli dzień mieści się w zakresie 1-31, jest poprawny
elif month == 4 or month == 6 or month == 9 or month == 11:
    # Miesiące z 30 dniami: kwiecień, czerwiec, wrzesień, listopad
    if day >= 1 and day <= 30:
        day_ok = True  # Jeśli dzień mieści się w zakresie 1-30, jest poprawny
elif month == 2:
    # Luty standardowo ma 28 dni
    if day >= 1 and day <= 28:
        day_ok = True  # Jeśli dzień mieści się w zakresie 1-28, jest poprawny

# Przygotuj wiadomość do wyświetlenia
message = 'Day ' + str(day) + ' for the month ' + str(month)

# Wyświetl odpowiedni komunikat w zależności od poprawności dnia
if day_ok:
    print(f'{message} is correct')  # Jeśli dzień jest poprawny, wyświetl odpowiedni komunikat
else:
    print(f'{message} is incorrect')  # Jeśli dzień jest niepoprawny, wyświetl odpowiedni komunikat
