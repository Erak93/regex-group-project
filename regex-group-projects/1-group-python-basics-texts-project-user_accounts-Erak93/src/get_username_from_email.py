import re


def get_username_from_email():
    email=input("Give me your email")
    sear=re.search('(\w+)(@.+)',email).group(1)
    if sear:
        print(sear)
    else:
        print("no data")    
     

    
get_username_from_email()

 