#This is a mini project to correctly reqognize the email format
#module 
import re
#function
def validate_email(email):
    pattern = r'^\w+@[a-zA-Z]+\.[a-zA-Z]+$'
    
    if re.match(pattern, email):
        print("OK")
    else:
        print("WRONG")

#output
email = input("Enter your email: ")
validate_email(email)