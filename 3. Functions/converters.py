# Funkcja do konwersji metrów na centymetry
def m_to_cm(meters):
    return meters * 100

# Funkcja do konwersji centymetrów na metry
def cm_to_m(cm):
    return cm / 100

# Funkcja do konwersji centymetrów na cale
def cm_to_inch(cm):
    return cm / 2.54  # 1 cal = 2.54 cm

# Funkcja do konwersji stóp i cali na centymetry
def feet_inches_to_cm(feet, inches):
    total_inches = (feet * 12) + inches  # Konwertowanie stóp na cale i dodanie cali
    cm = total_inches * 2.54  # Konwersja cali na centymetry
    return cm

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f"60cm = {cm_to_inch(60)}inches")
    print(f"7 feet and 6 inches is {feet_inches_to_cm(7,6)} cm")
