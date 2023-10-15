
def find_union(list1, list2):
    union = list1.copy()
    for item in list2:
        if item not in union:
            union.append(item)
    return union


def find_intersection(list1, list2):
    intersection = []
    for item in list1:
        if item in list2:
            intersection.append(item)
    return intersection


def find_difference(list1, list2):
    difference = []
    for item in list1:
        if item not in list2:
            difference.append(item)
    return difference


list1 = []


n = int(input("Enter number of elements for list-1 : "))


for i in range(0, n):
    ele = int(input())

    list1.append(ele)

list2 = []


n = int(input("Enter number of elements for list-2 : "))


for i in range(0, n):
    ele = int(input())

    list2.append(ele)


union_result = find_union(list1, list2)
intersection_result = find_intersection(list1, list2)
difference_result = find_difference(list1, list2)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)
