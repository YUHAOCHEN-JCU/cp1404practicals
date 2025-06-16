"""
numbers is empty list
repeat i 5 times
    get number
    append number in numbers
first_number = numbers[0]
last_number = numbers[4]
smallest_number = minimum number in numbers
largest_number = maximum number in numbers
average = total of numbers/length of numbers
print first_number, last_number, smallest_number, largest_number, average

display usernames
get username
if username in usernames
    display "Access granted"
else
    display "Access denied"
"""
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
first_number = numbers[0]
last_number = numbers[4]
smallest_number = min(numbers)
largest_number = max(numbers)
average = sum(numbers)/len(numbers)
print(f"The first number is {first_number}")
print(f"The last number is {last_number}")
print(f"The smallest number is {smallest_number}")
print(f"The largest number is {largest_number}")
print(f"The average of the numbers is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter your name: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
