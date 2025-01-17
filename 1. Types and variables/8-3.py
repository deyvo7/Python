###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = float(input("Enter temperature in Celsius: "))

kelvin = celsius + 273.15
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equivalent to {kelvin:.2f}K and {fahrenheit:.2f}°F")