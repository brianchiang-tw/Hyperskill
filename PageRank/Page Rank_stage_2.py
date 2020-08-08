import numpy as np
import numpy.linalg as la
from io import StringIO

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


# initial vector for r
r = ( np.ones(6) / 6 ) * 100.0

# ------------------------------------
# for r_1

r_1 = np.matmul(L, r)
print_mat(r_1)

# ------------------------------------
# for r_11

r_next = r_1
for _ in range(10):
    r_next = np.matmul(L, r_next)

r_11 = r_next
print_mat(r_11)

# ------------------------------------
# for r_convergence under diff < 0.01


r_cur = r
threshold = 0.01
while True:

    r_next = np.matmul(L, r_cur)

    if la.norm(r_next - r_cur) < threshold:
        # check convergence condition is met or not
        break

    r_cur = r_next

print_mat(r_cur)
