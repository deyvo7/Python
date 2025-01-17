class Square:
    # Konstruktor inicjalizujący bok kwadratu
    def __init__(self, a):
        self.a = a  # Przechowuje długość boku kwadratu
    
    # Metoda do obliczania powierzchni kwadratu
    def area(self):
        return self.a * self.a  # Pole kwadratu to bok * bok
    
    # Metoda do obliczania obwodu kwadratu
    def perimeter(self):
        return self.a * 4  # Obwód kwadratu to 4 * bok

# Tworzymy obiekty klasy Square
square1 = Square(4)  # Kwadrat o boku 4
square2 = Square(6)  # Kwadrat o boku 6

# Wyświetlamy wyniki dla kwadratu o boku 4
print('Kwadrat o boku 4:')
print(f'Pole wynosi {square1.area()}, Obwód wynosi {square1.perimeter()}')

# Wyświetlamy wyniki dla kwadratu o boku 6
print('Kwadrat o boku 6:')
print(f'Pole wynosi {square2.area()}, Obwód wynosi {square2.perimeter()}')
