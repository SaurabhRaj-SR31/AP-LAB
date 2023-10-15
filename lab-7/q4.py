import re
f = open("C:/Users/Saurabh Raj/Desktop/python/lab-7/inputmail.txt", 'r')
f1 = open("C:/Users/Saurabh Raj/Desktop/python/lab-7/validmail.txt", 'w')
f2 = open("C:/Users/Saurabh Raj/Desktop/python/lab-7/invalidmail.txt", 'w')


lst = f.readlines()
pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
for line in lst:
    if re.match(pat, line):
        f1.write(line)

    else:
        f2.write(line)
f.close()
f1.close()
f2.close()