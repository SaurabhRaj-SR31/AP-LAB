def product(num):
    r = 1
    for n in num:
        r = r*n

    return r


if __name__ == "__main__":
    lst = []


n = int(input("Enter number of elements : "))


for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print(product(lst))
