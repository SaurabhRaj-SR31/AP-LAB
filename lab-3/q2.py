def unique(l):

    list_set = set(l)
    unique_list = (list(list_set))
    print(unique_list)


if __name__ == "__main__":
    lst = []


n = int(input("Enter number of elements : "))


for i in range(0, n):
    ele = int(input())

    lst.append(ele)

unique(lst)
