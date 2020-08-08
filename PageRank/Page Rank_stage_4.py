import numpy as np
import numpy.linalg as la
from io import StringIO

def print_mat(mat):

    stream = StringIO()
    np.savetxt(stream, mat, fmt="%.3f")
    print( stream.getvalue() )

# -----------------------------------

def get_convergent_vector(L, r_0, threshold=0.01):

    '''
    :param L: transition matrix
    :param r_0: initial vector
    :param threshold: parameter for convergence condition
    :return: convergent vector
    '''

    r_cur = r_0

    while True:

        r_next = np.matmul(L, r_cur)

        if la.norm(r_next - r_cur) < threshold:
            # check convergence condition is met or not
            break

        r_cur = r_next

    return r_cur

# -----------------------------------
def get_matrix_with_damping(matrix, damping=0.5):

    # get the size of matrix
    n, _ = matrix.shape
    
    return matrix * damping + ( 1 - damping ) * np.ones((n, n)) / n



# -----------------------------------

tokens = input().split()
n, damping_factor = int( tokens[0] ), float( tokens[1] )


matrix = [ [ 0.0 for x in range(n)] for y in range(n) ]

for y in range(n):
    matrix[y] = [ *map( float, input().split() ) ]



# convert to numpy array
matrix = np.array(matrix)

matrix_with_damping = get_matrix_with_damping(matrix, damping=damping_factor)

r_0 = ( np.ones(n) / n) * 100

# compute pagerank
r_pagerank = get_convergent_vector(L=matrix_with_damping, r_0=r_0, threshold=0.01)

# output result
print_mat(r_pagerank)

