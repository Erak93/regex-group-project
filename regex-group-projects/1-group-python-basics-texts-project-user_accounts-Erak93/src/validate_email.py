import re

"""""
def validate_email():
    while True:
        email_input=input("Please digit your email")
        test=re.search(r'[a-zA-Z]{1}[a-zA-Z_.+-]{0,}\w+@[a-zA-Z_-].+[a-zA-Z]',email_input)
        if test:
            print("Thank you for the email")
            break
        else:
            print("Wrong Format")
"""

#WORK IN PROGRESS: DO NOT TOUCH!





validate_email()






"""
    Email validation rules:
        - Case insensitive
        - Starts with a letter
        - At least two characters before the @
        - The characters before the @ are letters, digits, underscore '_', dash '-', and dot '.'
        - after the @ the characters accepted are letters, digits, underscore '_', dash '-', and dot '.'
        - after the @ there can't be 2 dots in a row '..'
        - The email address end with a dot followed by 2 to 5 letters. Example ".me", ".com", ".euro" ".rugby"

    :param email_input: <str> The string to be checked
    :return: True if email_input respects the email format. Returns False otherwise
    """
    


