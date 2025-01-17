# Klasa reprezentująca profil na mediach społecznościowych
class SocialMediaProfile:
    # Konstruktor klasy, inicjalizujący nazwę użytkownika oraz listę postów
    def __init__(self, username):
        self.username = username  # Nazwa użytkownika
        self.posts = []  # Lista postów

    # Metoda dodająca nowy post do profilu użytkownika
    def add_post(self, content):
        self.posts.append(content)  # Dodaj post do listy
        print(f"{self.username} dodał nowy post: {content}")

    # Metoda wyświetlająca timeline użytkownika, z numerowanymi postami
    def display_timeline(self):
        print(f"Posty użytkownika {self.username}: ")
        # Użycie enumerate do numerowania postów
        for index, post in enumerate(self.posts, start=1):
            print(f"{index}. {post}")  # Wyświetl post z numerem

# Tworzymy obiekt użytkownika o nazwie 'johndoe'
user1 = SocialMediaProfile("johndoe")

# Dodajemy posty
user1.add_post("Hello, world!")
user1.add_post("Had a great day at the park!")
user1.add_post("What's up, Natalie? How are you?")

# Wyświetlamy timeline użytkownika
user1.display_timeline()
