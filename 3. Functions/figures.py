import turtle

# Rysowanie kwadratu o podanej długości boku
def draw_square(length):
    for _ in range(4):
        turtle.forward(length)  # Przesuń żółwia do przodu o długość boku
        turtle.right(90)       # Obróć żółwia o 90 stopni w prawo

# Rysowanie trójkąta równobocznego o podanej długości boku
def draw_triangle(length):
    for _ in range(3):
        turtle.forward(length)  # Przesuń żółwia do przodu o długość boku
        turtle.right(120)       # Obróć żółwia o 120 stopni w prawo

# Rysowanie prostokąta o podanych długościach boków
def draw_rectangle(length_a, length_b):
    for _ in range(2):
        turtle.forward(length_a)  # Przesuń żółwia do przodu o długość boku a
        turtle.right(90)          # Obróć żółwia o 90 stopni w prawo
        turtle.forward(length_b)  # Przesuń żółwia do przodu o długość boku b
        turtle.right(90)          # Obróć żółwia o 90 stopni w prawo
