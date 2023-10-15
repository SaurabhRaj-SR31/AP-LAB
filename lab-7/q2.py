f = open("C:/Users/Saurabh Raj/Desktop/python/lab-7/data.txt", 'r')
dic = {}
for line in f.readlines():

    line = line.strip("\n")
    lst = line.split()
    for word in lst:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
print(dic)

f.close()
