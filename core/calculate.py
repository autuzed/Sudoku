import numpy as np


def check_row(x, i):
    for n in A[i - 1, 0:9]:
        if x == n:
            return False
    return True


def check_col(x, j):
    for n in A[0:9, j - 1]:
        if x == n:
            return False
    return True


def check_box(x, b):
    i2 = int((b / 3 if int(b / 3) == (b / 3) else int(b / 3) + 1) * 3)
    i1 = i2 - 3
    j2 = b % 3 * 3 if b % 3 != 0 else 9
    j1 = j2 - 3
    print(A[i1:i2, j1:j2])
    for n in np.array(A[i1:i2, j1:j2]).reshape((1, 9))[0]:
        if x == n:
            return False
    return True


# 创建矩阵
A = [[0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, ]]

A = np.array(A)
A = np.diag((1, 2, 3, 4, 5, 6, 7, 8, 9))
A[6:9, 3:6] = 1
# print(check_box(0, 9))
print(check_box(5, 9))
