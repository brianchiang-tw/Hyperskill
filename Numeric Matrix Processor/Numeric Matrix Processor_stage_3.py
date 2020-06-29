def get_matrix(msg1, msg2, mode):

    print(msg1)


    h, w = map(int,input().split())

    matrix = [ [] for _ in range(h) ]

    print(msg2)
    for y in range(h):

        if mode == "int":
            matrix[y] = [*map(int, input().split())]

        elif mode == "float":
            matrix[y] = [*map(float, input().split())]


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

                matrix_container[0] = get_matrix(msg_mat_1_size, msg_mat_1_content, "float")
                matrix_container[1] = get_matrix(msg_mat_2_size, msg_mat_2_content, "float")

                result = add_matrices(matrix_container[0], matrix_container[1])
                print_matrix(result)

            elif choice == 2:

                matrix_container[0] = get_matrix(msg_mat_size, msg_mat_content, "float")
                constant = get_constant()

                result = multiply_by_number(matrix_container[0], constant)
                print_matrix(result)

            elif choice == 3:
                matrix_container[0] = get_matrix(msg_mat_1_size, msg_mat_1_content, "float")
                matrix_container[1] = get_matrix(msg_mat_2_size, msg_mat_2_content, "float")

                result = multiply_by_matrix(matrix_container[0], matrix_container[1])
                print_matrix(result)

        except Exception as e:
            print(e)

# ---------------------------------------------------------

menu()

