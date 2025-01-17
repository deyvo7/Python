# Write a program that calculates a dog's age in dog's years.
# For the first two years, a dog's life is equal to 10.5 human years.
# After that, each dog year is equal to 4 human years. Sample result:

# Enter the dog's age in human years: 15
# The dog's age in dog's years is 73 years.

###
# Program obliczający wiek psa w latach psich
# Pierwsze dwa lata życia psa odpowiadają 10.5 roku życia człowieka
# Po dwóch latach każdy rok psa odpowiada 4 latach życia człowieka
###

# Pobranie wieku psa w latach ludzkich od użytkownika
age = int(input("Enter the dog's age in human years: "))
age_counter = 1  # Licznik lat psa
dog_years = 0.0  # Wiek psa w latach psich

# Pętla licząca wiek psa
while age_counter <= age:
    if age_counter <= 2:  # Pierwsze dwa lata życia psa
        dog_years += 10.5  # Każdy rok psa przez pierwsze dwa lata to 10.5 roku ludzkiego
    if age_counter > 2:  # Po dwóch latach życia psa
        dog_years += 4  # Każdy rok psa po dwóch latach to 4 lata ludzkie
    age_counter += 1  # Zwiększamy licznik lat

# Wyświetlenie wyniku
print(f"The dog's age in dog's years is {dog_years}")
