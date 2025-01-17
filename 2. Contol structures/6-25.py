# Write a program that creates the following pattern. Sample result:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# Program, który tworzy wzór z liczbami

for i in range(1, 10):  # Pętla dla liczb od 1 do 9
    print(str(i) * i)  # Wydrukuj liczbę i, powtarzaną i razy
