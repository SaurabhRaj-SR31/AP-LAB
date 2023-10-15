l1 = []


n = int(input("Enter number of elements for list-1 : "))


for i in range(0, n):
    ele = int(input())

    l1.append(ele)

l2 = []


n = int(input("Enter number of elements for list-2 : "))


for i in range(0, n):
    ele = int(input())

    l2.append(ele)
l3 = [n for n in l2 if n % 2]+[n for n in l1 if not n % 2]
print(l3)
