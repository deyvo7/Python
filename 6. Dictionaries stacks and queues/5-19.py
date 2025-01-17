import json

# Funkcja do wczytania danych z pliku JSON
def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Wczytuje dane z pliku JSON do zmiennej 'data'
    return data['reservations']  # Zwraca listę rezerwacji z danych

# Funkcja do obliczenia liczby wszystkich pokoi
def count_rooms(reservations):
    return len(reservations)  # Zwraca liczbę elementów w liście rezerwacji

# Funkcja do obliczenia liczby zapłaconych rezerwacji
def count_paid_reservations(reservations):
    paid_count = 0
    for reservation in reservations:  # Przechodzi przez każdą rezerwację
        if reservation['paid']:  # Jeśli rezerwacja jest opłacona
            paid_count += 1  # Zwiększa licznik zapłaconych rezerwacji
    return paid_count

# Funkcja do obliczenia liczby nieopłaconych rezerwacji
def count_unpaid_reservations(reservations):
    unpaid_count = 0
    for reservation in reservations:
        if not reservation['paid']:  # Jeśli rezerwacja nie jest opłacona
            unpaid_count += 1  # Zwiększa licznik nieopłaconych rezerwacji
    return unpaid_count

# Funkcja do obliczenia łącznej wartości zapłaconych rezerwacji
def total_paid_value(reservations):
    total_paid = 0
    for reservation in reservations:
        if reservation['paid']:  # Sprawdza tylko zapłacone rezerwacje
            total_paid += reservation['nights'] * reservation['price_per_night']  # Oblicza wartość rezerwacji
    return total_paid

# Funkcja do obliczenia łącznej wartości nieopłaconych rezerwacji
def total_unpaid_value(reservations):
    total_unpaid = 0
    for reservation in reservations:
        if not reservation['paid']:  # Sprawdza tylko nieopłacone rezerwacje
            total_unpaid += reservation['nights'] * reservation['price_per_night']  # Oblicza wartość rezerwacji
    return total_unpaid

# Główna funkcja programu
def main():
    # Wczytanie danych z pliku reservations.json
    reservations = load_reservations('reservations.json')

    # Obliczenie danych
    total_rooms = count_rooms(reservations)
    paid_reservations = count_paid_reservations(reservations)
    unpaid_reservations = count_unpaid_reservations(reservations)
    paid_value = total_paid_value(reservations)
    unpaid_value = total_unpaid_value(reservations)

    # Wyświetlenie wyników
    print(f'Liczba pokoi: {total_rooms}')
    print(f'Liczba zapłaconych rezerwacji: {paid_reservations}')
    print(f'Liczba nieopłaconych rezerwacji: {unpaid_reservations}')
    print(f'Łączna wartość zapłaconych rezerwacji: {paid_value} PLN')
    print(f'Łączna wartość nieopłaconych rezerwacji: {unpaid_value} PLN')

# Uruchomienie programu
if __name__ == '__main__':
    main()
