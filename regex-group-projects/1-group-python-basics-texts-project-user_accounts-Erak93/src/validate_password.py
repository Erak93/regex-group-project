import re


# Complete this function to check if passwords respect the format
def validate_password(pwd_input):
    test=re.search('^.*(?=.*[a-z])(?=.*[A_Z])(?=\w{8,30})(?=.*\d)(?=.*[!\*\-_\.]).*$',pwd_input)
    if test:
        return True

    return False


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





