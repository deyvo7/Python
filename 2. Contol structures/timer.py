###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
#
# Pobiera liczbę od użytkownika i odlicza do zera.
#
# Zmodyfikuj program, aby ostatnie pięć sekund odliczania
# było wyświetlane słownie, czyli pięć, cztery, trzy, dwa, jeden.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

# Odliczanie do zera
while countdown > 0:
    # Wyświetlanie ostatnich 5 sekund słownie
    if countdown <= 5:
        if countdown == 5:
            print("five")
        elif countdown == 4:
            print("four")
        elif countdown == 3:
            print("three")
        elif countdown == 2:
            print("two")
        elif countdown == 1:
            print("one")
    else:
        print(countdown)
    
    countdown -= 1
    time.sleep(1)  # Czekaj 1 sekundę

print("Time's up!")  # Koniec odliczania
