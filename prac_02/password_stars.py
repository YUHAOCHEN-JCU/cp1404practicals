def main():
    password = get_password()
    print(password)


def get_password():
    user_word = input("Please enter word: ")
    print("*" * len(user_word))
    return user_word


main()


