# A device in a door registers people entering and leaving a room.The + sign means a person entering a room
#  and the -- sign a person leaving a room. Define the function f(detector) that returns True if at least 3 people
# were in the room at the same time, or False otherwise. Sample result:

# f("+-+++-+---") returns True
# f("+-+-+-+-") returns False
# f("+-++-+--") returns False
# f("+-++-++-+---") returns True

def f(detector):
    # Zmienna do śledzenia aktualnej liczby osób w pokoju
    current_count = 0
    
    # Iteracja po każdym znaku w ciągu detector
    for action in detector:
        if action == '+':
            current_count += 1  # Osoba wchodzi do pokoju
        elif action == '-':
            current_count -= 1  # Osoba wychodzi z pokoju
        
        # Sprawdzenie, czy w danym momencie w pokoju jest co najmniej 3 osoby
        if current_count >= 3:
            return True
    
    # Jeśli pętla zakończy się i nigdy nie osiągnięto 3 osób, zwróć False
    return False

# Przykładowe testy
print(f("+-+++-+---"))  # Powinno zwrócić True
print(f("+-+-+-+-"))   # Powinno zwrócić False
print(f("+-++-+--"))   # Powinno zwrócić False
print(f("+-++-++-+---"))  # Powinno zwrócić True
