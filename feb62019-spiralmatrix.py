# Question 90 - Spiral matrix

# Given a matrix with m x n dimensions, print its elements in spiral form. For example, given:

# a = [ [10, 2, 11],
# [1, 3, 4],
# [8, 7, 9] ]


# Your function should return:

# 10, 2, 11, 4, 9, 7, 8, 1, 3

# Solution will be written in Python for premium users.

# Upgrade to premium to receive in-depth solutions to each problem.


def spiral_matrix(mat):
    n_rows = len(mat)
    n_cols = len(mat[0])

    for n in range(min(n_rows, n_cols) // 2 + 1):

        for item in mat[n][n:-1-n]:
            yield str(item)
        for item in (r[-1-n] for r in mat[n:-1-n]):
            yield str(item)
        for item in mat[-1-n][-1-n:n:-1]:
            yield str(item)
        for item in (r[n] for r in mat[-1-n:n:-1]):
            yield str(item)

    if n_cols == n_rows and n_rows % 2 != 0:
        yield str(mat[n_rows // 2][n_cols // 2])


if __name__ == "__main__":
    a = [[10, 2, 11],
         [1, 3, 4],
         [8, 7, 9]]
    print(''.join(spiral_matrix(a)))
    b = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 0, 'a', 'b'],
         ['c', 'd', 'e', 'f']]
    print(''.join(spiral_matrix(b)))
    c = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 0, 11, 12]]
    print(''.join(spiral_matrix(c)))

    d = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         ['a', 'b', 'c'],
         ['d', 'e', 'f']]
    print(''.join(spiral_matrix(d)))
