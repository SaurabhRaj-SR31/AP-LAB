def counter():
    a = 1
    b = "yes"
    c = 'Ram'


print("Number of local varibales available:", counter.__code__.co_nlocals)
