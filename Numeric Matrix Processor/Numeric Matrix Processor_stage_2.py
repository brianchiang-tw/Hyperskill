def get_matrix():

    h, w = map(int,input().split())

    matrix = [ [] for _ in range(h) ]

    for y in range(h):
        matrix[y] = [*map(int, input().split())]

    matrix_container[idx] = matrix

    return matrix

# ---------------------------------------------------------

def get_constant():

    return int(input())

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

def print_matrix( matrix):

    h, w = len(matrix), len(matrix[0])

    for y in range(h):
        for x in range(w):
            print(matrix[y][x], end=" ")

        print()

    return

# ---------------------------------------------------------


matrix_container = [None, None]

for idx in range(1):

    matrix = get_matrix()
    matrix_container[idx] = matrix

constant = get_constant()
first_matrix = matrix_container[0]

try:
    result = multiply_by_number(first_matrix, constant)
    print_matrix(result)

except Exception as e:
    print(e)
