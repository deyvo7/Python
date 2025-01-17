# In a separate module, define a function that checks if the number is within the range <x, y>.
# The function returns a boolean value. Then, create a program and use the function you defined. Sample result:

# A number: 7
# Number 7 in the range <2,15>: yes

from module_7_5 import is_within_range

def main():
    number = int(input("A number: "))
    x=2
    y=15  # Zakres do sprawdzenia

    if is_within_range(number, x, y):
        print(f"Number {number} in the range <{x}, {y}>: yes")
    else:
        print(f"Number {number} in the range <{x}, {y}>: no")

if __name__ == "__main__":
    main()
