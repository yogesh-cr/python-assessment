# Write a Python program to check the validity of password input by users. It should validate the password with given below conditions.

#    *At least 1 letter between [a-z] and 1 letter between [A-Z].
#    *At least 1 number between [0-9].
#    *At least 1 special character [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~].
#    *Minimum length 6 characters.
#    *Maximum length 16 characters.

import re
p= input("Input your password")
temp = True
while temp:  
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        temp=False
        break

if temp:
    print("Not a Valid Password")