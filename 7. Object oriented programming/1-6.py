class Phone:
    # Konstruktor inicjalizujący stan telefonu
    def __init__(self, battery_perc, charging, screen):
        self.battery_perc = battery_perc  # Procent naładowania baterii
        self.charging = charging  # Status ładowania (True/False)
        self.screen = screen  # Status ekranu (on/off)

    # Metoda do ładowania telefonu
    def charge_phone(self):
        self.charging = True  # Ustawia status ładowania na True
    
    # Metoda do wyłączania ekranu
    def turn_off_the_screen(self):
        self.screen = "off"  # Ustawia ekran na "off"
    
    # Metoda do obliczania pozostałego czasu pracy baterii
    def calculate_battery_time_left(self, rate):
        self.battery_life = self.battery_perc / rate  # Oblicza czas pracy baterii na podstawie tempa zużycia

    # Metoda do sprawdzania, czy telefon jest ładowany
    def check_if_charging(self):
        if self.charging:
            self.is_charging = "Yes"  # Jeśli ładuje się, ustaw "Yes"
        else:
            self.is_charging = "No"  # Jeśli nie ładuje się, ustaw "No"

# Tworzymy obiekt telefonu
my_phone = Phone(68, False, "On")

# Wywołanie metod na obiekcie telefonu
my_phone.turn_off_the_screen()  # Wyłączamy ekran
my_phone.charge_phone()  # Ładujemy telefon
my_phone.check_if_charging()  # Sprawdzamy, czy telefon się ładuje
# Obliczamy czas pracy baterii na podstawie tempa zużycia (wprowadź dane od użytkownika)
my_phone.calculate_battery_time_left(int(input("How many battery percentages do you lose per hour?: ")))

# Wyświetlamy informacje o telefonie
print(f"My phone's battery is at {my_phone.battery_perc}%. The screen of my phone is {my_phone.screen}. Is my phone being charged right now?: {my_phone.is_charging}. The battery will last for {my_phone.battery_life} hours.")
