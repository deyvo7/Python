# A lamp in a room has three light bulbs. Switch one lights one bulb, and switch two lights the other two bulbs.
# Write a program that tells you how many bulbs are lit, depending on the state of switch one and switch two.

###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
###
# Oświetlenie w domu z trzema żarówkami i dwoma przełącznikami
# Program sprawdza, ile żarówek jest włączonych, w zależności od stanu przełączników
###

# Stan przełączników (False - wyłączony, True - włączony)
light_switch1 = False  # Pierwszy przełącznik (włączony lub wyłączony)
light_switch2 = False  # Drugi przełącznik (włączony lub wyłączony)

# Zmienna do liczenia liczby włączonych żarówek
bulbs_on = 0

# Jeśli pierwszy przełącznik jest włączony, włączona jest jedna żarówka
if light_switch1:
    bulbs_on += 1

# Jeśli drugi przełącznik jest włączony, włączają się dwie żarówki
if light_switch2:
    bulbs_on += 2

# Wyświetlenie liczby włączonych żarówek
print(f"Bulbs on: {bulbs_on}")