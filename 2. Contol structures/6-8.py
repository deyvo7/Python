# Write a program that checks that both people are adults. Read people's data from the keyboard.

###
# Checking if both people are adults
#
###
# Program sprawdzający, czy obie osoby są dorosłe
# Program pobiera dane dwóch osób i sprawdza, czy obie są dorosłe (wiek >= 18)
###

# Pobranie imienia i wieku pierwszej osoby
person1_name = input("Enter the first person's name: ")
person1_age = int(input("Enter the first person's age: "))

# Pobranie imienia i wieku drugiej osoby
person2_name = input("Enter the second person's name: ")
person2_age = int(input("Enter second person's age: "))  

# Sprawdzanie, czy obie osoby są dorosłe
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')  # Obie osoby są dorosłe
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')  # Jedna z osób nie jest dorosła
