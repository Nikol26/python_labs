def check_rectangular(mat):
    if not mat:
        return True
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            return False
    return True
def row_sums(mat):
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    return [sum(row) for row in mat]
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))