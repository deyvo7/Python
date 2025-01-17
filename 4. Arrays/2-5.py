# The data below represents a cinema's seating arrangement. Write a program that:

# calculates how many seats are available
# calculates how many seats are booked
# informs what the status of a seat is in a given row and given place (available or booked)
# 5x5 cinema seating
# A = Available, B = Booked

# Rozmieszczenie miejsc w kinie (A - dostępne, B - zarezerwowane)
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Funkcja zwracająca całkowitą liczbę miejsc
def seats_total(seats):
   return len(seats) * len(seats[0])

# Funkcja zwracająca liczbę dostępnych miejsc
def seats_available(seats):
   available = 0
   for row in seats:
      for seat in row:
         if seat == 'A':  # Jeśli miejsce jest dostępne
            available += 1
   return available

# Funkcja zwracająca liczbę zarezerwowanych miejsc
def seats_booked(seats):
   booked = 0
   for row in seats:
      for seat in row:
         if seat == 'B':  # Jeśli miejsce jest zarezerwowane
            booked += 1
   return booked

# Funkcja zwracająca status miejsca (dostępne/zarezerwowane)
def seat_status(seats, row, place):
   if seats[row-1][place-1] == 'A':  # Indeksowanie od 0, więc odejmujemy 1
      return "Available"
   else:
      return "Booked"

# Wyświetlanie wyników
print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))  # Status miejsca w 1. rzędzie, 1. miejscu
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))  # Status miejsca w 5. rzędzie, 5. miejscu
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))  # Status miejsca w 3. rzędzie, 5. miejscu
