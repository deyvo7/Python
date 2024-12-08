###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
###
# Sprawdzanie, czy dostępna jest zniżka
# Zniżka przysługuje dzieciom poniżej 18 roku życia
# lub osobom w wieku 65 lat lub starszym.
###

# Pobierz wiek użytkownika
age = int(input('Enter your age: '))  # Wprowadź wiek (liczba całkowita)

# Sprawdź, czy użytkownik kwalifikuje się do zniżki
if age < 18 or age >= 65:
    print("eligible for discount")  # Jeśli użytkownik ma mniej niż 18 lat lub 65 lat i więcej, przysługuje mu zniżka
else:
    print("no discount")  # W przeciwnym razie zniżka nie przysługuje
