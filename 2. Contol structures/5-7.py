###
# The timer.py program takes a number from the user and counts down to zero.
# Modify the program so that the last five seconds of the counter are printed in words, i.e. five, four, three, two, one.

###
# Program timer.py, który odlicza od podanej liczby do zera
# Zmodyfikowany, aby ostatnie 5 sekund było wyświetlane słownie
###

# Pobranie liczby od użytkownika
number = int(input("Enter the number: "))  

# Pętla odliczająca od number do 1
for i in range(number, 0, -1):  
    if i > 5:  # Jeśli liczba jest większa niż 5, wyświetla ją numerycznie
        print(i)
    else:
        # Jeśli liczba jest 5 lub mniejsza, wyświetla ją słownie
        if i == 5:
            print("five")
        elif i == 4:
            print("four")
        elif i == 3:
            print("three")
        elif i == 2:
            print("two")
        elif i == 1:
            print("one")
