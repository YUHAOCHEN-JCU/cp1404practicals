"""
CP1404/CP5632 Practical
Data file -> lists program
FILENAME = "subject_data.txt"


function main()
    data = load_data()
    print_information(data)


function load_data()
    open FILENAME as input_file and read
    contents is empty list
    repeat line in input_file
        line = line remove the \n
        parts = parts separate the data into its parts
        make the number an integer
        append parts in contents
    close input_file
    return contents


function print_information(contents)
    repeat information in contents
        subject_code = information[0]
        name = information[1]
        student_number = information[2]
        print subject_code, name, student_number


main()
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_information(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    contents = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        contents.append(parts)
    input_file.close()
    return contents


def print_information(contents):
    """Print information based on list"""
    for information in contents:
        subject_code = information[0]
        name = information[1]
        student_number = information[2]
        print(f"{subject_code} is taught by Ada {name} and has {student_number}")


main()
