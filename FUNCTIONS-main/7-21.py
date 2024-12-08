# Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers.
# Sample result:

# f(7,4,9) returns 5
# f(2,12,8) returns 10

def f(number1, number2, number3):
    # Znajdujemy największą i najmniejszą liczbę spośród trzech podanych
    max_num = max(number1, number2, number3)
    min_num = min(number1, number2, number3)
    
    # Zwracamy różnicę między największą a najmniejszą liczbą
    return max_num - min_num

# Testowanie funkcji
print(f(7, 4, 9))  # Zwraca 5 (9 - 4)
print(f(2, 12, 8))  # Zwraca 10 (12 - 2)
