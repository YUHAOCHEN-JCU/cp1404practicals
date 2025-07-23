"""
function main()
    display "Let's drive!"
    taxis contain Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)
function display_menu
    display MENU
    current_taxi = None
    total_bill = 0.0
    display_menu()
    get user_choice
    while user_choice not equal to "q"
        if user_choice = "c"
            display_taxis(taxis)
            try
                get taxi_choice
                if 0 <= taxi_choice < len(taxis)
                    current_taxi = taxis[taxi_choice]
                else
                    display error message
            except ValueError
                display error message

        else if user_choice = "d"
            if current_taxi is None
                display "You need to choose a taxi before you can drive"
            else
                try
                    get distance
                    current_taxi.start_fare()
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    display current_taxi.name, trip_cost
                    total_bill = total_bill + trip_cost
                except ValueError
                    display error message

        else
            display "Invalid option"

        display total_bill
        display_menu()
        get user_choice

    display total_bill
    display "Taxis are now:"
    display_taxis(taxis)


function display_taxis(taxis)
    display "Taxis available:"
    repeat taxi in taxis with index i
        display i , taxi


main()
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")

    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0.0

    display_menu()
    user_choice = input(">>> ").lower()

    while user_choice != "q":
        if user_choice == "c":
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input; enter a number.")

        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    total_bill += trip_cost
                except ValueError:
                    print("Please enter a valid number.")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        display_menu()
        user_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_menu():
    print(MENU)


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
