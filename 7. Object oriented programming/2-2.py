# Definicja klasy Song, reprezentującej utwór muzyczny
class Song:
    # Konstruktor klasy, który ustawia początkowe wartości dla wykonawcy, tytułu, albumu i roku
    def __init__(self, performer, title, album, year):
        self.performer = performer  # Wykonawca utworu
        self.title = title          # Tytuł utworu
        self.album = album          # Nazwa albumu
        self.year = year            # Rok wydania utworu

    # Metoda __str__, która zwraca dane utworu w odpowiednim formacie
    def __str__(self):
        # Zwraca formatowaną informację o utworze
        return (f"Performer: {self.performer}\nTitle: {self.title}\nAlbum: {self.album}\nYear: {self.year}\n")

# Tworzenie obiektów reprezentujących dwa utwory muzyczne
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

# Użycie obiektów - drukowanie informacji o utworach
print(song1)  # Wydrukowanie informacji o pierwszym utworze
print(song2)  # Wydrukowanie informacji o drugim utworze
