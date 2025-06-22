"""
Program to process Wimbledon gentlemen's singles champions data.
Estimate time: 45 minutes
Actual time: 60 minutes
function main()
    filename = "wimbledon.csv"
    data = read_csv_data(filename)
    champion_wins = count_champion_wins(data)
    countries = get_champion_countries(data)
    display "Wimbledon Champions:"
    repeat champion, wins in items of champion_wins
        display champion, wins
    display countries


read_csv_data(filename)
    data is an empty list
    open filename as in_file and read
        lines = read each lines of in_file
        for index, line in enumerate of lines
            if index > 0
                parts is correct
                append parts in data
    return data


function count_champion_wins(data)
    champion_wins  is empty dictionary
    repeat row in data
        champion = row[2]
        if champion in champion_wins
            champion_wins[champion] = champion_wins[champion] + 1
        else
            champion_wins[champion] = 1
    return champion_wins


function get_champion_countries(data)
    countries = set()
    repeat row in data:
        country = row[3]
        add country in countries
    return sorted countries
"""


def main():
    """
    Orchestrate the processing and display of Wimbledon data.
    """
    filename = "wimbledon.csv"
    data = read_csv_data(filename)
    champion_wins = count_champion_wins(data)
    countries = get_champion_countries(data)
    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_csv_data(filename):
    """
    Read the Wimbledon CSV data file, skipping the header row without using continue.
    Return the data as a list of lists.
    """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        for index, line in enumerate(lines):
            if index > 0:
                parts = line.strip().split(",")
                data.append(parts)
    return data


def count_champion_wins(data):
    """
    Count how many times each champion has won.
    Return a dictionary with champion names as keys and win counts as values.
    """
    champion_wins = {}
    for row in data:
        champion = row[2]
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1
    return champion_wins


def get_champion_countries(data):
    """
    Extract the unique countries of the champions and sort them alphabetically.
    Return a sorted list of countries.
    """
    countries = set()
    for row in data:
        country = row[3]
        countries.add(country)
    return sorted(countries)


main()
