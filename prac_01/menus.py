"""
This program greets the user or gives prompts based on the input options (H/G/Q).
"""

"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

user_name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
user_choice = input(">>> ").upper()
while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {user_name}")
    elif user_choice == "G":
        print(f"Goodbye {user_name}")
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    user_choice = input(">>> ").upper()
print("Finished.")
