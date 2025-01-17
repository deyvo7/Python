# Write a program that draws the graph of the function f(x)=x2-3. Sample result:

import matplotlib.pyplot as plt

# Tworzymy listę x od -100 do 100 (włącznie)
x = []
for n in range(-100, 101):
    x.append(n)

# Tworzymy listę y dla każdej wartości x, stosując funkcję f(x) = x^2 - 3
y = []
for n in x:
    y.append(n**2 - 3)

# Rysujemy wykres
plt.plot(x, y)

# Dodajemy tytuł i etykiety osi
plt.title("Wykres funkcji f(x) = x^2 - 3")
plt.xlabel("x")
plt.ylabel("f(x)")

# Wyświetlamy wykres
plt.show()
