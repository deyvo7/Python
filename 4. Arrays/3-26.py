# Write a program that draws the function y = sin(x) for an angle value in the range 0-360 degrees.

import matplotlib.pyplot as plt
import numpy as np

# Tworzymy listę kątów w stopniach od 0° do 360°
angles_deg = np.linspace(0, 360, 361)

# Konwertujemy kąty na radiany
angles_rad = np.radians(angles_deg)

# Obliczamy wartości funkcji y = sin(x) dla każdego kąta
y_values = np.sin(angles_rad)

# Rysujemy wykres
plt.plot(angles_deg, y_values)

# Dodajemy tytuł oraz etykiety osi
plt.title("Wykres funkcji y = sin(x) w zakresie 0° - 360°")
plt.xlabel("Kąt (stopnie)")
plt.ylabel("y = sin(x)")

# Wyświetlamy wykres
plt.grid(True)  # Dodajemy siatkę do wykresu
plt.show()
