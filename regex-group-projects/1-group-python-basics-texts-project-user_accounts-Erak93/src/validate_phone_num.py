import re

def validate_phone_num():
        
   x=str(input("Digit phone number please"))
   search=re.search('\+\d{3}\s\(\d{3}\)\s\d{3}\s\d{4}',x)
   if search:
        print(True)
   else:
        print(False)     


  
validate_phone_num()
    
    
