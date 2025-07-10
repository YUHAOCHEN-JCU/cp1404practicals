"""
function main()
    guitars = load_guitars()
    display "guitars list"
    repeat guitar in guitars
        display guitar
    display "Please input guitar's information"
    get name
    while name
        get year, cost
        guitar = Guitar(name, year, cost)
        append guitar in guitars
        display guitar
        save_guitars(guitars)
        display"data has been saved in guitars.csv"


function load_guitars()
    guitars is an empty list
    try
        with open "guitars.csv" and read as file
            for line in file
                output name, year, cost
                guitars append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError
        display error message
    return guitars


function save_guitars(guitars)
    with open "guitar.csv" and write as file:
        repeat guitar in guitars
            write name, year, cost in file


main()

"""
from guitar import Guitar


def main():
    """The main function that drives the guitar data management process."""
    guitars = load_guitars()
    print("guitars list")
    for guitar in guitars:
        print(guitar)

    print("Please input guitar's information")

    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        save_guitars(guitars)
        print("data has been saved in guitars.csv")


def load_guitars():
    """Load guitar data from guitars.csv"""
    guitars = []
    try:
        with open("guitars.csv", "r") as file:
            for line in file:
                name, year, cost = line.strip().split(",")
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print("guitars.csv not found")
    return guitars


def save_guitars(guitars):
    """Save guitars data"""
    with open("guitar.csv", "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}\n")


main()
