#1
A = [[4, 3],[1, 1]]
def smallholder(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

print(smallholder(A))

#2
A = [[0, 2, 1],[1, 4, 3],[2, 1, 1]]
def submatrix(A, i, j):
    return [row[:j] + row[j+1:] for idx, row in enumerate(A) if idx != i]

print(submatrix(A, 0, 0))

#3
def determinate(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0
    for j in range(len(A)):
        det += ((-1) ** j) * A[0][j] * determinate(submatrix(A, 0, j))
    return det

B = [
    [0, 2, 1, 4],
    [1, 0, 3, 2],
    [0, 1, 4, 0],
    [1, 2, 1, 1]
]

print(determinate(B))

#4
def minor(A, i, j):
    return determinate(submatrix(A, i, j))

print(minor(B, 0, 1))

#5
def alg(A, i, j):
    return (-1)**(i+j) * minor(A, i, j)

print(alg(B, 1, 1))

#6
def algmatrix(A):
    n = len(A)
    Am = [[0] * n for _ in range(n)]
    for i in range(len(A)):
        for j in range(len(A)):
            Am[i][j] = alg(A, i, j)
    return Am

print(algmatrix(B))

#7
import numpy as np
def inv(A):
    return (np.transpose(algmatrix(A))/determinate(A))

print(inv(B))

#8
def moor_penrose(A):
    At = np.transpose(A)
    AtA = np.dot(At, A)
    inv_AtA = inv(AtA.tolist())
    return np.dot(inv_AtA, At)

print(moor_penrose(B))