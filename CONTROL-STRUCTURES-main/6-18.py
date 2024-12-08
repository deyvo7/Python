# Let x and y denote the coordinates of a point on the plane.
# Write a program that determines in which quadrant of the coordinate system the point P(x, y)
# is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.

# Sample result:
# x = 5
# y = 2
# Point P(5,2) is in the first quadrant of the coordinate system

# Program określający, w którym ćwiartce układu współrzędnych znajduje się punkt P(x, y)
# lub czy znajduje się na jednej z osi, lub w punkcie (0,0) układu współrzędnych.

# Pobranie współrzędnych punktu P
x = int(input("Enter the x-coordinate: "))  # Wczytanie współrzędnej x
y = int(input("Enter the y-coordinate: "))  # Wczytanie współrzędnej y

# Sprawdzenie, czy punkt P jest w punkcie (0,0)
if x == 0 and y == 0:
    location = "Point P(0,0) is at the origin of the coordinate system."
# Sprawdzenie, czy punkt P znajduje się na osi y
elif x == 0:
    location = f"Point P({x},{y}) is on the y-axis."
# Sprawdzenie, czy punkt P znajduje się na osi x
elif y == 0:
    location = f"Point P({x},{y}) is on the x-axis."
# Sprawdzenie, w której ćwiartce znajduje się punkt P
elif x > 0 and y > 0:
    location = f"Point P({x},{y}) is in the first quadrant of the coordinate system."
elif x < 0 and y > 0:
    location = f"Point P({x},{y}) is in the second quadrant of the coordinate system."
elif x < 0 and y < 0:
    location = f"Point P({x},{y}) is in the third quadrant of the coordinate system."
else:
    location = f"Point P({x},{y}) is in the fourth quadrant of the coordinate system."

# Wyświetlenie informacji o lokalizacji punktu
print(location)
