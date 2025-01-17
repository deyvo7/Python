import queue

"""
Kolejka to struktura danych, która działa na zasadzie
First In, First Out (FIFO), czyli pierwszy element,
który zostanie dodany do kolejki, będzie pierwszym, 
który zostanie z niej usunięty. Kolejka działa podobnie
do prawdziwej kolejki, na przykład linii ludzi czekających
na obsługę — osoba, która przyjdzie pierwsza, zostanie
obsłużona pierwsza.
"""

# Tworzymy kolejkę
people = queue.Queue()

# Dodajemy osoby do kolejki (na koniec kolejki)
people.put('Michael')    
people.put('Charlotte')  
people.put('Olivia')     

# Wypisujemy liczbę elementów w kolejce
print('Liczba elementów w kolejce:', people.qsize())

# Pobieramy i wypisujemy osoby z kolejki
while not people.empty():  # Dopóki kolejka nie jest pusta
    person = people.get()  # Usuwamy pierwszą osobę z kolejki
    print(person)  # Wypisujemy imię osoby
