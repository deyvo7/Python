class Employee:
    """
    Klasa Employee reprezentuje pracownika z danymi:
    - imię (name),
    - nazwisko (surname),
    - wiek (age),
    - staż pracy (seniority - liczba lat pracy).
    """

    def __init__(self, name, surname, age, seniority):
        """
        Konstruktor klasy Employee. Przyjmuje dane pracownika w ustalonej kolejności:
        - name: Imię pracownika (str)
        - surname: Nazwisko pracownika (str)
        - age: Wiek pracownika (int)
        - seniority: Staż pracy w latach (int)
        """
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        """
        Metoda zwracająca tekstową reprezentację obiektu.
        Jeśli pracownik jest pełnoletni (wiek >= 18):
        - Zwraca nazwisko, pierwszą literę imienia i staż pracy w WIELKICH LITERACH.
        W przeciwnym wypadku:
        - Zwraca nazwisko, pierwszą literę imienia i staż pracy w małych literach.
        """
        if self.age >= 18:
            # Pełnoletni: WIELKIE litery
            return f"{self.surname.upper()}{self.name[0].upper()}{self.seniority}"
        else:
            # Niepełnoletni: małe litery
            return f"{self.surname.lower()}{self.name[0].lower()}{self.seniority}"


# Przykłady użycia:
employee1 = Employee("Anna", "May", 17, 7)
employee2 = Employee("George", "Brown", 21, 4)

print(str(employee1))  # Wynik: "maya7"
print(str(employee2))  # Wynik: "BROWNG4"
