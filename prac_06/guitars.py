"""
    guitars is an empty list
    display "My guitars!"
    get name
    while name
        get year
        get cost
        guitar = Guitar(name, year, cost)
        append guitar iin guitars
        display guitar

    display information
    repeat i, guitar in guitars and start = 1
    if guitar is_vintage()
    vintage_string = "(vintage)"
    else
    vintage_string = ""
    display i, guitar name, year of guitar, cost of guitar, vintage_string
"""
from guitar import Guitar


guitars = []
print("My guitars!")

name = input("Name: ")
while name:
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.\n")

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, start=1):
    if guitar.is_vintage():
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10.2f}{vintage_string}")


