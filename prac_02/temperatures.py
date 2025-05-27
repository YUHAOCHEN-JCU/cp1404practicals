"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
MENU = C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit

function main()
    display MENU
    get choice
    while choice not equal to "Q"
        if choice = "C"
            convert celsius to fahrenheit()
        else if choice = "F"
            convert fahrenheit to celsius()
        else
            display error message
        display MENU
        get choice
    display "Thank you."


function convert celsius to fahrenheit()
    get celsius
    fahrenheit = celsius * 9.0 / 5 + 32
    display fahrenheit


function convert fahrenheit to celsius()
    get fahrenheit
    celsius = 5 / 9 * (fahrenheit - 32)
    display celsius


main()
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """display menu to convert temperatures until quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

