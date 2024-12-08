# Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs.
#  Write a program that prints a survey consisting of three questions.
# Save the answers to logical type variables. Then view the survey result.

# Sample result:
# SURVEY Are you interested in computer science? (y/n): y
# Do you like playing computer games? (y/n): n
# Do you have an Instagram account? (y/n): y

# SURVEY RESULTS Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes

# Program przeprowadzający ankietę składającą się z trzech pytań
# Odpowiedzi są przechowywane w zmiennych logicznych, które będą użyte do wyświetlenia wyników.

print("SURVEY")

# Pobieranie odpowiedzi na pytania ankiety (y/n)
comp_sci = input("Are you interested in computer science? (y/n): ").strip().lower() == 'y'
comp_games = input("Do you like playing computer games? (y/n): ").strip().lower() == 'y'
insta = input("Do you have an Instagram account? (y/n): ").strip().lower() == 'y'

# Wyświetlenie wyników ankiety
print("\nSURVEY RESULTS")

# Sprawdzanie odpowiedzi na każde pytanie i wyświetlanie wyników
if comp_sci:
    print("Interested in computer science: Yes")
else:
    print("Interested in computer science: No")

if comp_games:
    print("Playing computer games: Yes")
else:
    print("Playing computer games: No")

if insta:
    print("Has an Instagram account: Yes")
else:
    print("Has an Instagram account: No")
