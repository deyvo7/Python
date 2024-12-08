import figures
import turtle

# Ustawienie ekranu
window = turtle.Screen()
window.bgcolor("lightgreen")

# Tworzenie żółwia
pen = turtle.Turtle()
pen.speed(5)

# Rysowanie kwadratu w dwóch różnych miejscach
pen.penup()
pen.goto(-150, 100)
pen.pendown()
figures.draw_square(100)

pen.penup()
pen.goto(150, -100)
pen.pendown()
figures.draw_square(100)

# Rysowanie trójkąta w dwóch różnych miejscach
pen.penup()
pen.goto(-200, -50)
pen.pendown()
figures.draw_triangle(100)

pen.penup()
pen.goto(200, 150)
pen.pendown()
figures.draw_triangle(100)

# Rysowanie prostokąta w dwóch różnych miejscach
pen.penup()
pen.goto(-100, -150)
pen.pendown()
figures.draw_rectangle(150, 75)

pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_rectangle(150, 75)

# Ukrycie żółwia i zakończenie programu
pen.hideturtle()
window.mainloop()
