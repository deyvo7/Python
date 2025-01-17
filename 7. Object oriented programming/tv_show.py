import tv  # Importujemy klasę TV z pliku tv.py

def main():
    # Tworzymy obiekt telewizora
    my_tv = tv.TV()

    # Wyświetlamy status telewizora (czy jest włączony czy wyłączony)
    print("Tworzymy telewizor")
    my_tv.show_status()

    # Włączamy telewizor i wyświetlamy jego status
    my_tv.turn_on()
    print("Włączamy telewizor")
    my_tv.show_status()

    # Ustawiamy dostępne kanały i wyświetlamy je
    channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
    my_tv.set_channels(channels)
    my_tv.show_channels()

    # Zmieniamy kanał na 4 (TVN) i wyświetlamy status
    my_tv.set_channel(4)  # Przechodzimy na kanał 4 (TVN)
    my_tv.show_status()

    # Zwiększamy głośność i wyświetlamy status
    my_tv.increase_volume()
    my_tv.show_status()

    # Zmniejszamy głośność i wyświetlamy status
    my_tv.decrease_volume()
    my_tv.show_status()

    # Wyłączamy telewizor i wyświetlamy jego status
    my_tv.turn_off()
    print("Wyłączamy telewizor")
    my_tv.show_status()

if __name__ == "__main__":
    main()  # Uruchamiamy główną funkcję programu
