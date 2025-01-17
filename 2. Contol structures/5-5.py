###
# Sums numbers entered by user
#
###
# Sumuje liczby wprowadzone przez użytkownika
###

# Zmienna do przechowywania sumy liczb
total_sum = 0  
# Zmienna do przechowywania średniej arytmetycznej
arithmetic_mean = 0  
# Zmienna do liczenia wprowadzonych liczb
numbers = 0  

# Pętla, która trwa w nieskończoność, aż użytkownik wprowadzi 0
while True:  
    # Prosi użytkownika o wpisanie liczby
    number = int(input("Enter a number (0 to stop): "))  
    
    # Jeśli użytkownik wprowadzi 0, pętla zostanie przerwana
    if number == 0:  
        break  # Zatrzymanie pętli, gdy 0 jest wprowadzone
    
    # Dodanie liczby do sumy
    total_sum += number  
    # Zwiększenie liczby wprowadzonych liczb
    numbers += 1  

# Obliczenie średniej arytmetycznej
arithmetic_mean = total_sum / numbers  
# Wyświetlenie sumy i średniej
print(f"The total sum of the numbers is: {total_sum} and the arithmetic mean is: {arithmetic_mean}")
