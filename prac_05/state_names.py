"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
display CODE_TO_NAME

get state_code
while state_code not equal to ""
    try
        display state_code with value
    except KeyError
        display error message
    get state_code
repeat state_code, full_state_name in key of CODE_TO_NAME and value of CODE_TO_NAME
    display state_code, full_state_name
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
for state_code, full_state_name in CODE_TO_NAME.items():
    print(f"{state_code:<3} is {full_state_name}")
