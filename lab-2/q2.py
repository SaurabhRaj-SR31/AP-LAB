def read_matrix(order):
    matrix = {}
    for i in range(order):
        for j in range(order):
            value = int(input(f"Enter the value at position ({i}, {j}): "))
            if value != 0:
                matrix[(i, j)] = value
    return matrix


def add_matrices(matrix1, matrix2):
    result_matrix = {}
    for key in matrix1:
        if key in matrix2:
            result_matrix[key] = matrix1[key] + matrix2[key]
        else:
            result_matrix[key] = matrix1[key]
    for key in matrix2:
        if key not in matrix1:
            result_matrix[key] = matrix2[key]
    return result_matrix


def convert_to_matrix(matrix_dict, order):
    matrix = [[0 for _ in range(order)] for _ in range(order)]
    for key, value in matrix_dict.items():
        i, j = key
        matrix[i][j] = value
    return matrix


if __name__ == "__main__":
    order = int(input("Enter the order of the matrices: "))

    print("Enter values for the first matrix:")
    matrix1 = read_matrix(order)

    print("Enter values for the second matrix:")
    matrix2 = read_matrix(order)

    result_matrix_dict = add_matrices(matrix1, matrix2)

    print("Result in dictionary form:")
    print(result_matrix_dict)

    result_matrix = convert_to_matrix(result_matrix_dict, order)

    print("Result in two-dimensional matrix form:")
    for row in result_matrix:
        print(row)
