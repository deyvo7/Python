###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# Load the temperature in degress Celsius
celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
# Calculate the temperature in Kelvins
kelvin = celsius + 273.15
# Calculate the temperature in Fahrenheits
Fahrenheit = (celsius * 9/5) + 32
# Display Results
print(f"Temperatura w kelvinach wynosi: {kelvin:.2f} K")
print(f"Temperatura w Fahrenheitach: {Fahrenheit:.2f} °F")