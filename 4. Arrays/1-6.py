# Write a program that prints the name of the day of the week for a given day number.
# Then, using the defined function, print the name of the day of the week
# for the following day numbers: 1, 4, 7.

###
# Returns the name of the day of the week for
# a given day number (1-Monday ... 7-Sunday)
#

# Funkcja zwraca nazwę dnia tygodnia dla podanego numeru dnia (1-Poniedziałek ... 7-Niedziela)
def weekday(n):
    # Lista nazw dni tygodnia
    weekdays = ["Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]  # Zwracamy odpowiedni dzień, indeksując od 0 (n-1)

# Wypisujemy nazwę dnia tygodnia dla wybranych numerów dni
print(weekday(1))  # Dla dnia 1 (Poniedziałek)
print(weekday(4))  # Dla dnia 4 (Czwartek)
print(weekday(7))  # Dla dnia 7 (Niedziela)
