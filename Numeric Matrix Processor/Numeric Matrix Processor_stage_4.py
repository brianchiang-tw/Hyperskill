def get_matrix(msg1, msg2, type):

    print(msg1)


    h, w = map(int,input().split())

    matrix = [ [] for _ in range(h) ]

    print(msg2)
    for y in range(h):

        matrix[y] = [*map(type, input().split())]



    return matrix

# ---------------------------------------------------------

def get_constant():
    print("Enter constant:")
    return float(input())

# ---------------------------------------------------------

def add_matrices( matrix_1, matrix_2 ):

    h_1, w_1 = len(matrix_1), len(matrix_1[0])
    h_2, w_2 = len(matrix_2), len(matrix_2[0])

    if (h_1 != h_2) and (w_1 != w_2):
        raise Exception('ERROR')

    result = [[0 for _ in range(w_1) ] for _ in range(h_1) ]

    for y in range(h_1):
        for x in range(w_1):
            result[y][x] = matrix_1[y][x] + matrix_2[y][x]

    return result

# ---------------------------------------------------------

def multiply_by_number( matrix_1, constant ):

    h_1, w_1 = len(matrix_1), len(matrix_1[0])

    result = [[0 for _ in range(w_1) ] for _ in range(h_1) ]

    for y in range(h_1):
        for x in range(w_1):
            result[y][x] = constant * matrix_1[y][x]

    return result

# ---------------------------------------------------------

def multiply_by_matrix( matrix_1, matrix_2 ):

    h_1, w_1 = len(matrix_1), len(matrix_1[0])
    h_2, w_2 = len(matrix_2), len(matrix_2[0])

    if w_1 != h_2:
        raise Exception("Error")


    result = [[0 for _ in range(w_2) ] for _ in range(h_1) ]

    for y in range(h_1):
        for x in range(w_2):
            result[y][x] = sum([matrix_1[y][k] * matrix_2[k][x] for k in range(w_1)])

    return result

# ---------------------------------------------------------

def transpose_by_main_diagonal( matrix_1 ):

    h, w = len(matrix_1), len(matrix_1[0])
    h_res, w_res = w, h

    result = [[0 for _ in range(w_res)] for _ in range(h_res)]

    for x in range(w_res):
        for y in range(h_res):
            result[y][x] = matrix_1[x][y]

    return result

# ----------------------------------------------------------

def transpose_by_side_diagonal( matrix_1 ):

    h, w = len(matrix_1), len(matrix_1[0])
    h_res, w_res = w, h

    result = [[0 for _ in range(w_res)] for _ in range(h_res)]

    for y in range(h):
        for x in range(w):
            result[w-1-x][h-1-y] = matrix_1[y][x]

    return result

# ----------------------------------------------------------

def transpose_by_vertical_line( matrix_1 ):

    h, w = len(matrix_1), len(matrix_1[0])

    result = [[0 for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            result[y][x] = matrix_1[y][w-1-x]

    return result

# ----------------------------------------------------------

def transpose_by_horizontal_line( matrix_1 ):

    h, w = len(matrix_1), len(matrix_1[0])

    result = [[0 for _ in range(w)] for _ in range(h)]

    for y in range(h):
        for x in range(w):
            result[y][x] = matrix_1[h-1-y][x]

    return result

# ---------------------------------------------------------

def print_matrix( matrix):

    print("The result is:")

    h, w = len(matrix), len(matrix[0])

    for y in range(h):
        for x in range(w):
            print(matrix[y][x], end=" ")

        print()


    print() # new line after result output

    return

# ---------------------------------------------------------

def menu():

    msg = """1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit
Your choice:"""

    msg_mat_size = "Enter size of matrix:"
    msg_mat_content = "Enter matrix"

    msg_mat_1_size = "Enter size of first matrix:"
    msg_mat_2_size = "Enter size of second matrix:"

    msg_mat_1_content = "Enter first matrix:"
    msg_mat_2_content = "Enter second matrix:"

    choice = -1

    while choice != 0:

        print(msg)

        try:

            choice = int(input())
            matrix_container = [None, None]
            if choice == 1:

                matrix_container[0] = get_matrix(msg_mat_1_size, msg_mat_1_content, float)
                matrix_container[1] = get_matrix(msg_mat_2_size, msg_mat_2_content, float)

                result = add_matrices(matrix_container[0], matrix_container[1])
                print_matrix(result)

            elif choice == 2:

                matrix_container[0] = get_matrix(msg_mat_size, msg_mat_content, float)
                constant = get_constant()

                result = multiply_by_number(matrix_container[0], constant)
                print_matrix(result)

            elif choice == 3:
                matrix_container[0] = get_matrix(msg_mat_1_size, msg_mat_1_content, float)
                matrix_container[1] = get_matrix(msg_mat_2_size, msg_mat_2_content, float)

                result = multiply_by_matrix(matrix_container[0], matrix_container[1])
                print_matrix(result)

            elif choice == 4:

                msg_transpose = ['1. Main diagonal','2. Side diagonal', '3. Vertical line', '4. Horizontal line']
                print()
                print('\n'.join(msg_transpose))
                print("Your choice")
                choice_of_transpose = int(input())

                if choice_of_transpose == 1:
                    matrix_container[0] = get_matrix("Enter matrix size", "Enter matrix", float)
                    result = transpose_by_main_diagonal(matrix_container[0])
                    print_matrix(result)

                elif choice_of_transpose == 2:
                    matrix_container[0] = get_matrix("Enter matrix size", "Enter matrix", float)
                    result = transpose_by_side_diagonal(matrix_container[0])
                    print_matrix(result)

                elif choice_of_transpose == 3:
                    matrix_container[0] = get_matrix("Enter matrix size", "Enter matrix", float)
                    result = transpose_by_vertical_line(matrix_container[0])
                    print_matrix(result)

                elif choice_of_transpose == 4:
                    matrix_container[0] = get_matrix("Enter matrix size", "Enter matrix", float)
                    result = transpose_by_horizontal_line(matrix_container[0])
                    print_matrix(result)




        except Exception as e:
            print(e)

# ---------------------------------------------------------

menu()
