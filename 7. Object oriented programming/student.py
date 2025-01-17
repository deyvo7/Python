# Klasa reprezentująca studenta
class Student():
    # Konstruktor inicjalizujący dane studenta
    def __init__(self):
        self.name = ""    # Imię studenta
        self.age = 0      # Wiek studenta
        self.id = 0       # Numer ID studenta
        self.major = ""   # Kierunek studiów (nowy atrybut)

def main():
    # Tworzenie obiektów dla trzech studentów
    student1 = Student()
    student2 = Student()
    student3 = Student()

    # Przypisanie wartości dla wszystkich atrybutów
    student1.name = "Dominic"
    student1.age = 19
    student1.id = 231624
    student1.major = "Computer Science"  # Przypisanie kierunku dla studenta 1

    student2.name = "Olivia"
    student2.age = 21
    student2.id = 351245
    student2.major = "Biology"  # Przypisanie kierunku dla studenta 2

    student3.name = "John"
    student3.age = 20
    student3.id = 324881
    student3.major = "Literature"  # Przypisanie kierunku dla studenta 3

    # Wyświetlanie informacji o studentach
    print('LISTA STUDENTÓW')
    print('================')
    print(f'{student1.name}, {student1.age} lat, nr ID: {student1.id}, Kierunek: {student1.major}')
    print(f'{student2.name}, {student2.age} lat, nr ID: {student2.id}, Kierunek: {student2.major}')
    print(f'{student3.name}, {student3.age} lat, nr ID: {student3.id}, Kierunek: {student3.major}')

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
