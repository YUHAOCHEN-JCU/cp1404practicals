"""
function main()
    password = get_password()
    display password


function get password()
    get user word
    display information
    return user word


main()
"""
def main():
    """print "*" based on user input"""
    password = get_password()
    print(password)


def get_password():
    """get user input and print "*" based on user word"""
    user_word = input("Please enter word: ")
    print("*" * len(user_word))
    return user_word


main()
