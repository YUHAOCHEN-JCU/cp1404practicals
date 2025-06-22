"""
function main()
    email_to_name = {}
    get email
    while email not equal to ""
        extracted_name = extract_name_from_email(email)
        get confirmation
        if confirmation = 'n' or confirmation = 'no'
            get name
        else
            name = extracted_name
        email_to_name[email] = name
        get email
    print()
    repeat email, name in items of email_to_name
        display name, email


function extract_name_from_email(email)
    get local_part, parts
    return "repeat part in parts"


main()
"""
def main():
    """Main function to collect emails and names, then print them."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        extracted_name = extract_name_from_email(email)
        confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()
        if confirmation == 'n' or confirmation == 'no':
            name = input("Name: ").strip()
        else:
            name = extracted_name
        email_to_name[email] = name
        email = input("Email: ").strip()
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extracts a likely name from the email address."""
    local_part = email.split('@')[0]
    parts = local_part.replace('.', ' ').replace('_', ' ').split()
    return ' '.join([part.title() for part in parts])


main()


