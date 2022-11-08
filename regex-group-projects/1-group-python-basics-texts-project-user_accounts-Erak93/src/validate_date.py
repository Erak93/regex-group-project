import re


def validate_date():
    date_input=input("give me a date")
    sear=re.search('(0?[1-9]|[12][0-9]|3[01])([-\/.])(0?[1-9]|1[012])([-\/.])(19[0-9][0-9]|20[0-9][0-9])',date_input) 
    print(bool(sear))
    
    
    
validate_date()    
