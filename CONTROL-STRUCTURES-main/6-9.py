# Most female names in Polish end with the letter "a".
# Write a program that prints the name entered from the keyboard, provided it is a female name.

# Sample result:
# Enter name: Anna
# Anna -- Polish female name

###
# Program, który sprawdza, czy podane imię jest typowym imieniem kobiecym w Polsce
# Większość imion kobiecych w Polsce kończy się literą "a"
###

# Pobranie imienia od użytkownika
name = input("Enter a name: ")

# Sprawdzamy, czy ostatnia litera imienia to "a"
if name[-1] == "a":
    # Jeśli ostatnia litera to "a", wypisujemy, że to imię kobiece
    print(f"{name} -- Polish female name")
