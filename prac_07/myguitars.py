from guitar import Guitar


def main():
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
    with open("guitar.csv", "w") as file:
        for guitar in guitars:
            file.write(f"{guitar.name}, {guitar.year}, {guitar.cost}\n")


main()
