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
            convert_celsius_to_fahrenheit()
        elif choice == "F":
            convert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit():
    """convert celsius to fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def convert_fahrenheit_to_celsius():
    """convert fahrenheit to celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()

