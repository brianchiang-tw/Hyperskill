import numpy as np
import numpy.linalg as la
from io import StringIO

#def print_mat(stream, mat):
def print_mat(mat):

    stream = StringIO()
    np.savetxt(stream, mat, fmt="%.3f")
    print( stream.getvalue() )

# -----------------------------------

# transition matrix L
L = np.array([
    [0,   1/2, 1/3, 0, 0,   0   ],
    [1/3, 0,   0,   0, 1/2, 0   ],
    [1/3, 1/2, 0,   1, 0,   1/2 ],
    [1/3, 0,   1/3, 0, 1/2, 1/2 ],
    [0,   0,   0,   0, 0,   0   ],
    [0,   0,   1/3, 0, 0,   0   ]
])

# output transition matrix
print_mat(mat=L)



#  compute eigenvalue and eigenvector
e_val, e_vacs = la.eig(L)

# take the eigenvector with eigenvalue = 1
vec = np.transpose(e_vacs)[0]

#  take only real part
vec_real = vec.real
vec_real = vec_real * 100.0/sum(vec_real)

# output eigenvector
print_mat(mat=vec_real)

