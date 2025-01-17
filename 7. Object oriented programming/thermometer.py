import random

class Thermometer:
    def __init__(self):
        """Inicjalizuje termometr, stan jest początkowo wyłączony"""
        self.is_on = False  # Termometr początkowo jest wyłączony
        self.temperature = None  # Temperatura początkowo nie jest zmierzona

    def turn_on(self):
        """Włącza termometr"""
        self.is_on = True
        print("Termometr włączony.")

    def turn_off(self):
        """Wyłącza termometr"""
        self.is_on = False
        print("Termometr wyłączony.")

    def measure_temperature(self):
        """Mierzy temperaturę, generując losową wartość w zakresie 34.0 - 42.0 stopni Celsjusza"""
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)  # Losujemy temperaturę z dokładnością do 0.1 stopnia
            print(f"Zmierzona temperatura: {self.temperature}°C")
        else:
            print("Termometr jest wyłączony. Włącz go, aby zmierzyć temperaturę.")

    def display_temperature(self):
        """Wyświetla zmierzoną temperaturę, ewentualnie komunikaty o gorączce lub temperaturze krytycznej"""
        if self.temperature is not None:
            if self.temperature >= 41.0:
                print(f"Temperatura: {self.temperature}°C - CRITICAL TEMPERATURE!!")
            elif self.temperature >= 37.0:
                print(f"Temperatura: {self.temperature}°C - Fever")
            else:
                print(f"Temperatura: {self.temperature}°C")
        else:
            print("Brak zmierzonej temperatury.")

