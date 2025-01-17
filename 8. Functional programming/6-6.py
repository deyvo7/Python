# Lista danych pracowników
employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
             ("Jackson","Peter"),("Johnson","Rick"),
             ("Lewis","Terry"),("Clarke","Robin")]

# Używamy map() oraz lambda, aby stworzyć nową listę z nazwiskami zapisanymi wielkimi literami
# i imionami, oddzielonymi przecinkiem
formatted_employees = list(map(lambda x: f"{x[0].upper()}, {x[1]}", employees))

# Wypisujemy wynik
for employee in formatted_employees:
    print(employee)
