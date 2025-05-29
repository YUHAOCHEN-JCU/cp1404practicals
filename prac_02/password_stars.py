"""
CP1404/CP5632 - Practical
Ask user's score and print "*" based on user input.
function main()
    get user word
    password = get password(user word)
    display password


function get password()
    return length of user word


main()
"""


def main():
    """Ask user's score and print "*" based on user input."""
    user_word = input("Please enter word: ")
    password = get_password(user_word)
    print(password * "*")


def get_password(user_word):
    """Return length of user word"""
    return len(user_word)


main()
