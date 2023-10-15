f = open("C:/Users/Saurabh Raj/Desktop/python/lab-7/data.txt", 'r')
w = 0
c = 0
l = 0
for line in f.readlines():
    l += 1
    line = line.strip("\n")
    lst = line.split()
    w += len(lst)
    for word in lst:
        c += len(word)

print(f"lines={l}")
print(f"words={w}")
print(f"characters={c}")
f.close()
