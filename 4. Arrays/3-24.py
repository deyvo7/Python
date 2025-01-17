# Familiarise yourself with methods of visualizing data:

# https://www.w3schools.com/python/matplotlib_intro.asp

# Then, using ‘matplotlib’, draw a line in a diagram from position (1, 3) to position (8, 10).
# Hint: to use 'matplotlib' in your programs, first you have to install the module by using the 'pip' command (python package manager).

# https://pythonguides.com/how-to-install-matplotlib-python/

# import matplotlib.pyplot as plt
# xpoints = [1, 8]
# ypoints = [3, 10]
# plt.plot(xpoints, ypoints)
# plt.show()

# komenda do zainstalowania: pip3 install matplotlib

# Importujemy bibliotekę do rysowania wykresów
import matplotlib.pyplot as plt

# Określamy punkty (x, y), przez które ma przejść linia
xpoints = [1, 8]  # współrzędne x punktów
ypoints = [3, 10]  # współrzędne y punktów

# Rysujemy wykres łącząc punkty
plt.plot(xpoints, ypoints)

# Wyświetlamy wykres
plt.show()
