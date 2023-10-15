def print_pascals_triangle(n):
    for line in range(n):
        coef = 1
        for i in range(1, n - line + 1):
            print(" ", end="")

        for j in range(0, line + 1):
            print(coef, end=" ")
            coef = coef * (line - j) // (j + 1)

        print()


n = int(input("enter no. : "))
print_pascals_triangle(n)
