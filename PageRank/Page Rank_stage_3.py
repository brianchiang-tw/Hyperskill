import numpy as np
import numpy.linalg as la
from io import StringIO

def print_mat(mat):

    stream = StringIO()
    np.savetxt(stream, mat, fmt="%.3f")
    print( stream.getvalue() )

# -----------------------------------

def get_convergent_vector(L, r_0, threshold):

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

# transition matrix L
L_without_damping = np.array([
    [0,   1/2, 1/3, 0, 0,   0,   0 ],
    [1/3, 0,   0,   0, 1/2, 0,   0 ],
    [1/3, 1/2, 0,   1, 0,   1/3, 0 ],
    [1/3, 0,   1/3, 0, 1/2, 1/3, 0 ],
    [0,   0,   0,   0, 0,   0,   0 ],
    [0,   0,   1/3, 0, 0,   0,   0 ],
    [0,   0,   0,   0, 0,   1/3, 1 ],
])

h, w = L_without_damping.shape

if h != w:
    raise Exception('transition matrix should be a square matrix.')

n = h

# damping factor
d = 0.5

L_with_damping = L_without_damping * d + (1-d)/n * np.ones(n)



# initial vector for r
r_0 = ( np.ones(n) / n ) * 100.0

# ------------------------------------

print_mat(L_without_damping)

result_without_damping = get_convergent_vector(L_without_damping, r_0, threshold=0.01)
print_mat(result_without_damping)

result_with_damping = get_convergent_vector(L_with_damping, r_0, threshold=0.01)
print_mat(result_with_damping)



