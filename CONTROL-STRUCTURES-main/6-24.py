# Write a program that creates the following pattern. Sample result:

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# Program, który tworzy wzór w kształcie piramidy

for i in range(1, 6):  # Pętla dla pierwszej części wzoru (rosnące gwiazdki)
    print('* ' * i)  # Wydrukuj odpowiednią liczbę gwiazdek

for i in range(4, 0, -1):  # Pętla dla drugiej części wzoru (malejące gwiazdki)
    print('* ' * i)  # Wydrukuj odpowiednią liczbę gwiazdek
