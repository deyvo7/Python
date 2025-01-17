# The data below represents monthly expenses divided into categories and weeks.
# 
# Write a program that calculates and prints:
# total expenses for each category
# total expenses for each week
# total expenses for a month

# Miesięczne wydatki podzielone na kategorie i tygodnie
monthly_expenses = [
   [200, 50, 100],  # Tydzień 1: [jedzenie, transport, media]
   [180, 60, 110],  # Tydzień 2
   [220, 55, 105],  # Tydzień 3
   [210, 65, 95]    # Tydzień 4
]

# Inicjalizacja zmiennych, które będą przechowywały sumy wydatków
food = 0
transport = 0
utilities = 0
week1 = 0
week2 = 0 
week3 = 0
week4 = 0
month = 0

# Obliczanie sumy wydatków na jedzenie w całym miesiącu
i = 0
while i <= (len(monthly_expenses)-1):
    food += monthly_expenses[i][0]  # Dodajemy wydatki na jedzenie z danego tygodnia
    i += 1  # Przechodzimy do następnego tygodnia

# Obliczanie sumy wydatków na transport w całym miesiącu
i = 0
while i <= (len(monthly_expenses)-1):
    transport += monthly_expenses[i][1]  # Dodajemy wydatki na transport z danego tygodnia
    i += 1  # Przechodzimy do następnego tygodnia

# Obliczanie sumy wydatków na media w całym miesiącu
i = 0
while i <= (len(monthly_expenses)-1):
    utilities += monthly_expenses[i][2]  # Dodajemy wydatki na media z danego tygodnia
    i += 1  # Przechodzimy do następnego tygodnia

# Obliczanie sumy wydatków w każdym tygodniu
for item in monthly_expenses[0]:  # Tydzień 1
    week1 += item  # Dodajemy wszystkie wydatki z tego tygodnia

for item in monthly_expenses[1]:  # Tydzień 2
    week2 += item  # Dodajemy wszystkie wydatki z tego tygodnia

for item in monthly_expenses[2]:  # Tydzień 3
    week3 += item  # Dodajemy wszystkie wydatki z tego tygodnia

for item in monthly_expenses[3]:  # Tydzień 4
    week4 += item  # Dodajemy wszystkie wydatki z tego tygodnia

# Obliczanie całkowitych wydatków na cały miesiąc
for row in monthly_expenses:  # Przechodzimy przez każdy tydzień
    for item in row:  # Przechodzimy przez wydatki w każdym tygodniu
        month += item  # Dodajemy każdy wydatek do całkowitej sumy

# Drukowanie wyników
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food)  # Wydatki na jedzenie
print('Transport:', transport)  # Wydatki na transport
print('Utilities:', utilities)  # Wydatki na media
print('Week 1:', week1)  # Wydatki w tygodniu 1
print('Week 2:', week2)  # Wydatki w tygodniu 2
print('Week 3:', week3)  # Wydatki w tygodniu 3
print('Week 4:', week4)  # Wydatki w tygodniu 4
print('---------------')
print('TOTAL:', month)  # Całkowite wydatki na cały miesiąc
