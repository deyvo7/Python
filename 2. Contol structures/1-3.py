###
# Sprawdzanie, czy samochód przekroczył dozwoloną prędkość
###

# Ustawienie maksymalnej dozwolonej prędkości (w km/h)
speed_limit = 140

# Wczytanie prędkości samochodu od użytkownika
car_speed = int(input('Enter car speed (km/h): '))

# Sprawdzenie, czy prędkość samochodu przekracza dozwoloną prędkość
if car_speed > 140:
    # Jeśli prędkość jest większa niż dozwolona, wyświetl prędkość samochodu
    print(f'Your speed is {car_speed}km/h')
    # Wyświetlenie komunikatu o przekroczeniu dozwolonej prędkości
    print('Warning: speed limit exceeded!!')
