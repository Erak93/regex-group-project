import re


# Complete this function to check if passwords respect the format
def validate_password(pwd_input):
    test=re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_\.!*])[A-Za-z\d\-\.!\*_]{8,30}$',pwd_input)
    if test:
        return True

    return False


print(validate_password("Madisson45!"))







"""
    At least 8 characters
    At most 30 characters
    At least one Uppercase
    At least one lowercase
    At least one digit
    At least one special character *, !, -, _, .
    Only accept the characters mentioned above

    :param pwd_input:
    :return: True if the pwd_input respect the pattern, False otherwise
    """
pass





