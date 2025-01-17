from thermometer import Thermometer  # Importujemy klasę Thermometer z pliku thermometer.py

def main():
    # Tworzymy obiekt termometru
    thermometer = Thermometer()
    
    # Włączamy termometr
    thermometer.turn_on()
    
    # Mierzymy temperaturę
    thermometer.measure_temperature()
    
    # Wyświetlamy zmierzoną temperaturę z odpowiednim komunikatem
    thermometer.display_temperature()
    
    # Wyłączamy termometr
    thermometer.turn_off()

if __name__ == "__main__":
    main()  # Uruchamiamy główną funkcję programu
