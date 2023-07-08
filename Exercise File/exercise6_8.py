# Create a user password
# import secrets and string
import secrets
import string
# This variable includes numbers
digits = string.digits
# This variable includes lowercase letters
s_letters = string.ascii_lowercase
# This variable includes uppercase
u_letters = string.ascii_uppercase
# This variable includes symbols
symbols = "-_~?*$#!+%@"
# only ask user for length of password
length = int(input("Choose the Password Length?\n"))
# shuffle all the variables
if length < 8:
    print("Password length must be more than 8!")
    pass
else:
    password = ''.join(secrets.choice(digits + s_letters + u_letters + symbols) for t in range(length))
    # print password
    print(f"Password:{password}")
