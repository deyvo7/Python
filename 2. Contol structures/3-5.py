###
# Calculates the number of days in a month
#
###
# Oblicza liczbę dni w miesiącu
###

# Pobierz numer miesiąca od użytkownika
month = int(input('Enter month number (1..12): '))  # Wprowadź numer miesiąca (od 1 do 12)

# Sprawdź liczbę dni w miesiącu
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31  # Miesiące z 31 dniami: styczeń, marzec, maj, lipiec, sierpień, październik, grudzień
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30  # Miesiące z 30 dniami: kwiecień, czerwiec, wrzesień, listopad
elif month == 2:
    days = 28  # Luty: standardowo ma 28 dni
    # Uwaga: nie sprawdzamy tutaj lat przestępnych
else:
    days = "error"
    print("That month doesn't exist")  # Obsługa sytuacji, gdy użytkownik wprowadzi niepoprawny numer miesiąca

# Wyświetl liczbę dni w podanym miesiącu
print(f'Month {month} has {days} days')  # Informacja o liczbie dni w miesiącu
