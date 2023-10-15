class Subset:
    def generator(self, input_list):
        mainlist = []
        for i in range(1 << len(input_list)):
            sublist = []
            for j in range(len(input_list)):
                if ((1 << j) & i == 0):
                    sublist.append(input_list[j])
            mainlist.append(sublist)
        return mainlist


if __name__ == "__main__":
    n = int(input("enter no. of elements :"))
    input_list = []
    for i in range(n):
        ele = int(input())
        input_list.append(ele)

    obj = Subset()
    final = []
    final = obj.generator(input_list)
    print(final, end=",")