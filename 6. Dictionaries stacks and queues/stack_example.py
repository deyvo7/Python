import queue

# Tworzymy stos
stack = queue.LifoQueue()

# Dodajemy elementy na stos
stack.put(2)  # Dodajemy 2
stack.put(3)  # Dodajemy 3
stack.put(7)  # Dodajemy 7
stack.put(4)  # Dodajemy 4
stack.put(1)  # Dodajemy 1
stack.put(9)  # Dodajemy 9
stack.put(8)  # Dodajemy 8

# Sumujemy dwa ostatnie elementy ze stosu i wyświetlamy wynik
last = stack.get()  # Pobieramy ostatni element ze stosu
second_last = stack.get()  # Pobieramy przedostatni element
sum_last_two = last + second_last  # Sumujemy oba elementy
print('Suma dwóch ostatnich liczb:', sum_last_two)

# Zwracamy przedostatni element na stos (ponieważ chcemy zachować stos, z wyjątkiem dwóch ostatnich elementów)
stack.put(second_last)

# Obliczamy sumę pozostałych elementów na stosie przy użyciu pętli 'while'
total_sum = 0
while not stack.empty():  # Dopóki stos nie jest pusty
    total_sum += stack.get()  # Dodajemy element do sumy

print('Suma pozostałych elementów stosu:', total_sum)
