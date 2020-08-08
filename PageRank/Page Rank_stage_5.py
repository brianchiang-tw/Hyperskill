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

# get the size
n = int( input() )

# get the name of website
websites = input().split()

# get transition matrix
matrix = [ [ 0.0 for x in range(n)] for y in range(n) ]

for y in range(n):
    matrix[y] = [ *map( float, input().split() ) ]

# get the name of target website
target = input()

# convert to numpy array
matrix = np.array(matrix)

matrix_with_damping = get_matrix_with_damping(matrix, damping=0.5)

r_0 = ( np.ones(n) / n) * 100

# compute pagerank
r_pagerank = get_convergent_vector(L=matrix_with_damping, r_0=r_0, threshold=0.01)

# output result


web_pagerank_dict = {}
for idx in range(n):
    web_pagerank_dict[ websites[idx] ] = r_pagerank[idx]

# target is always on the top
result = [ target ]

# remove target from dictionary
del web_pagerank_dict[target]

# sorted by pagerank and name of website in ascending order
for website in sorted(web_pagerank_dict, key=lambda w: (web_pagerank_dict[w], w), reverse=True):
    result.append( website )

# output top 5 results
for idx, website in enumerate(result):

    if idx < 5:
        print(website)
    else:
        break

