import re
str = input("enter string :")
reg = r'^[a-z]$|^([a-z]).*\1$'
if (re.search(reg, str)):
    print(f"yes {str} is a palindrome !")
else:
    print(f"no {str} is a palindrome !")
