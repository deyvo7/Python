# Write a program that prints a lottery coupon (numbers from 1 to 49) in the format as below.

# 1 8 15 22 29 36 43
# 2 9 16 23 30 37 44
# 3 10 17 24 31 38 45
# 4 11 18 25 32 39 46
# 5 12 19 26 33 40 47
# 6 13 20 27 34 41 48
# 7 14 21 28 35 42 49

# Program do generowania kuponu lotto

# Pętla iterująca przez 7 wierszy
for i in range(1, 8):
    # Pętla iterująca przez 7 liczb w każdym wierszu
    for j in range(0, 7):
        print(i + j * 7, end=' ')  # Obliczenie i wydrukowanie liczby
    print()  # Przejście do nowego wiersza po każdym zestawie liczb
