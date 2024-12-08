# Write a program that asks the user for their age and then checks which age group they belong to:

# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
# Senior: 65 or older

###
# Program sprawdzający grupę wiekową użytkownika
# Grupy wiekowe:
# Dziecko: poniżej 13 roku życia
# Nastolatek: od 13 do 19 roku życia
# Dorosły: od 20 do 64 roku życia
# Senior: 65 lat lub starszy
###

# Pobranie wieku użytkownika
age = int(input("Enter your age: "))

# Sprawdzanie, do jakiej grupy wiekowej należy użytkownik
if age >= 65:
    print("You're a senior")  # Użytkownik jest seniorem, jeśli ma 65 lat lub więcej
elif age >= 20:
    print("You're an adult")  # Użytkownik jest dorosły, jeśli ma od 20 do 64 lat
elif age >= 13:
    print("You're a teen")  # Użytkownik jest nastolatkiem, jeśli ma od 13 do 19 lat
elif age < 13 :
    print("You're a child")  # Użytkownik jest dzieckiem, jeśli ma mniej niż 13 lat
