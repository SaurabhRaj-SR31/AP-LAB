from module1 import reverse_string


def is_palindrome(s):

     s = s.replace(" ", "").lower()
     str=s
     return (str == reverse_string(s))


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
