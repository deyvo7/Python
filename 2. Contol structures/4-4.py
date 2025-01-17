###
# Prints the name of university where you are studying
# with an extra space between characters (add a space between
# each character)
#
###
# Wyświetla nazwę uniwersytetu, na którym studiujesz,
# z dodatkową spacją pomiędzy literami (dodaj spację po każdej literze)
###

# Nazwa uniwersytetu
university = 'Krakow University of Economics'

# Zmienna do przechowywania przekształconej nazwy
university_expanded = ''

# Iteracja przez każdy znak w nazwie uniwersytetu
for x in university:
    university_expanded = university_expanded + x + ' '  # Dodaj znak i spację

# Wyświetl oryginalną nazwę
print(university)  
# Wyświetl przekształconą nazwę z dodatkowymi spacjami
print(university_expanded)
