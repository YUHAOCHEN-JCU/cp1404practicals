"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
function main()
    incomes = get_user_incomes()
    print_income_report(incomes)


function get_user_incomes()
    user_incomes is empty list
    get add_months

    repeat month from 1 to add_month + 1
        get income
        append income in user_incomes

    return user_incomes


function print_income_report(user_incomes)
    print information
    total = 0
    repeat month from 1 to length of user_incomes + 1
        income = user_incomes[month - 1]
        total = total + income
        print month, income, total
"""
def main():
    """Main function to handle income report generation."""
    incomes = get_user_incomes()
    print_income_report(incomes)


def get_user_incomes():
    """Prompt user for number of months and income for each month. Return list of incomes."""
    user_incomes = []
    add_months = int(input("How many add_months? "))

    for month in range(1, add_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        user_incomes.append(income)

    return user_incomes


def print_income_report(user_incomes):
    """Print a formatted income report based on user incomes."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(user_incomes) + 1):
        income = user_incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
