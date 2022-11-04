import re


def get_numbers():
    string="On 26th of March the Witcher decided it was time to earn money. He only had 30 kronas left. He went to a small city which required his help. The reward was set to 100 kronas, but after a short but convincing discussion with soltys it was raised to 300 kronas."
    print(re.findall('\d+',string))


get_numbers()