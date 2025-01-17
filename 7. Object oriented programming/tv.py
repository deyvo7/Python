class TV:
    def __init__(self):
        # Inicjalizujemy telewizor: wyłączony, kanał 1, brak dostępnych kanałów oraz poziom głośności 0
        self.is_on = False  # Telewizor jest wyłączony
        self.channel_no = 1  # Domyślnie ustawiamy kanał na 1
        self.channels = []  # Lista dostępnych kanałów jest pusta na początku
        self.volume = 0  # Głośność ustawiona na 0

    def turn_on(self):
        """Włącza telewizor."""
        self.is_on = True  # Ustawiamy stan telewizora na włączony

    def turn_off(self):
        """Wyłącza telewizor."""
        self.is_on = False  # Ustawiamy stan telewizora na wyłączony

    def show_status(self):
        """Wyświetla aktualny status telewizora: włączony lub wyłączony oraz informacje o kanale i głośności, jeśli telewizor jest włączony."""
        if self.is_on:
            # Jeżeli telewizor jest włączony, wyświetlamy numer kanału i jego nazwę (jeśli kanał jest dostępny)
            channel_name = self.channels[self.channel_no - 1] if self.channel_no <= len(self.channels) else "Unknown"
            print(f"TV jest włączony, kanał {self.channel_no} ({channel_name}), głośność {self.volume}")
        else:
            # Jeżeli telewizor jest wyłączony, tylko informujemy o tym
            print("TV jest wyłączony")

    def set_channel(self, new_channel_no):
        """Ustawia nowy numer kanału."""
        # Sprawdzamy, czy podany numer kanału mieści się w dostępnych kanałach
        if 1 <= new_channel_no <= len(self.channels):
            self.channel_no = new_channel_no  # Ustawiamy kanał
        else:
            print("Niepoprawny numer kanału!")  # Jeśli kanał jest niepoprawny, wyświetlamy błąd

    def set_channels(self, channels_list):
        """Ustawia listę dostępnych kanałów."""
        self.channels = channels_list  # Ustawiamy listę dostępnych kanałów

    def show_channels(self):
        """Wyświetla listę dostępnych kanałów."""
        print("Lista kanałów:")
        for i, channel in enumerate(self.channels, 1):
            print(f"{i}. {channel}")  # Wypisujemy każdy kanał z numerem

    def increase_volume(self):
        """Zwiększa głośność o 1, ale nie przekracza maksymalnej wartości 10."""
        if self.volume < 10:
            self.volume += 1  # Zwiększamy głośność

    def decrease_volume(self):
        """Zmniejsza głośność o 1, ale nie spada poniżej 0."""
        if self.volume > 0:
            self.volume -= 1  # Zmniejszamy głośność
