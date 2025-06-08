"""
FILENAME_1 = "name.txt"
FILENAME_2 = "numbers.txt"

get name
open FILENAME_1 as file and write name in file
close file

open FILENAME_2 as content and read
close file
display content

open FILENAME_2 as file and read
number_1 = the first line number
number_2 = the second line number
close file
result = number_1 + number_2
display result

total = 0
with open FILENAME_2 as file and read
    repeat line in file
        number = line's integer
        total = total + number
        print total
"""
FILENAME_1 = "name.txt"
FILENAME_2 = "numbers.txt"

name = input("Please enter your name: ")
file = open(FILENAME_1, "w")
file.write(name)
file.close()

file = open(FILENAME_2, "r")
content = file.read()
file.close()
print(f"Hi {content}")

file = open(FILENAME_2, "r")
number_1 = int(file.readline().strip())
number_2 = int(file.readline().strip())
file.close()
result = number_1 + number_2
print(result)

total = 0
with open(FILENAME_2, "r") as file:
    for line in file:
        number = int(line.strip())
        total += number
    print(total)